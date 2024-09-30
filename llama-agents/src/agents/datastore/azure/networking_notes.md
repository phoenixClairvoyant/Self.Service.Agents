# Networking Notes
These notes are meant for anyone who wishes to get a quic grasp of important, but often misunderstood or forgotten networking concepts in general and specifically relating to Azure.

## Subnets
[Subnetting](https://en.wikipedia.org/wiki/Subnetwork)
refers to dividing one network into multiple sub networks through specifying multiple network prefixes  for housing their own sets of host identifiers.

[Classless Inter-domain Routing or CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
was introduced in 1993 by the Internet Engineering Task Force to tackle the problem of IP address exhaustion and large routing tables.
Before CIDR, the network prefix component in the most significant bit part of the IPv4 address
was composed of 8 bit increments only, so the 32 total bits could have one of 8, 16 or 24 bits allocated for this.
CIDR relaxed this and introduced variable length network prefix such that the notation 192.168.4.0/22 refers to a CIDR address block with  
22 bits allocated to the network prefix part and the remaining 10 bits to the host identifier part (in the least significant bits).
The notation 192.168.4.0/22 thus refers to 
addresses in the range 192.168.4.0 through 192.168.4.255,
as well as addresses in the range 192.168.5.0 through 192.168.5.255,
as well as addresses in the range 192.168.6.0 through 192.168.6.255,
as well as addresses in the range 192.168.7.0 through 192.168.7.255.

## Virtual Network
[Virtual Networks or VNets in Azure](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) 
is a free service and should be used to secure and organise resources from a network perspective.
[Azure Virtual Network best practices](https://learn.microsoft.com/en-us/azure/virtual-network/concepts-and-best-practices)
provide some guidance on things to keep in mind when setting up a VNet:
*  Ensure non-overlapping address spaces. Make sure your VNet address space (CIDR block) does not overlap with your organization's other network ranges.
* Your subnets should not cover the entire address space of the VNet. Plan ahead and reserve some address space for the future.
* It is recommended you have fewer large VNets rather than multiple small VNets. This will prevent management overhead.
* Secure your VNets by assigning Network Security Groups (NSGs) to the subnets beneath them. For more information about network security concepts, see Azure network security overview.

[Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview)
seems to imply that once a resource is added to a VNet, 
if that resource establishes a connection to any other Azure resource (even though a public IP/FQDN) then traffic is routed through the Azure backbone.

 > If the destination address is for one of Azure's services, Azure routes the traffic directly to the service over Azure's backbone network, rather than routing the traffic to the Internet. 
> Traffic between Azure services doesn't traverse the Internet, regardless of which Azure region the virtual network exists in, or which Azure region an instance of the Azure service 
> is deployed in. 

## Virtual Network Service Endpoint
[Azure virtual network service endpoints | Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview)
provides a good overview on the whole concept of Service Endpoints.
Much of these notes came from there.

* A Virtual Network Service Endpoint (or Service Endpoint) is a configuration set on a subnet of a VNet for a specific PaaS product such as cloud storage, database-as-a-service and so forth..
* A virtual network service endpoint provides the identity of your virtual network to the Azure service. 
* Without a Service Endpoint set, a resource in a VNet accesses a PaaS using the resource's public IP as source, and the PaaS public IP as destination.
* With a Service Endpoint set, a resource in a VNet accesses a PaaS using the resource's private IP on the VNet subnet as source, and the PaaS public IP as destination.
* Once you enable service endpoints in your virtual network, you can add a virtual network rule to secure the Azure service resources to your virtual network.
* With service endpoints, service traffic switches to use virtual network private addresses as the source IP addresses when accessing the Azure service from a virtual network. 
* This switch allows you to access the services without the need for reserved, public IP addresses used in IP firewalls.
* There's no extra charge for using service endpoints. 
* There's no limit on the total number of service endpoints in a virtual network.

Azure [puts it this way](https://learn.microsoft.com/en-us/azure/virtual-network/vnet-integration-for-azure-services#compare-private-endpoints-and-service-endpoints):

> Service endpoints provide secure and direct connectivity to Azure services over the Azure backbone network.
>  Endpoints allow you to secure your Azure resources to only your virtual networks.
>  Service endpoints enable private IP addresses in the VNet to reach an Azure service without the need of an outbound public IP.
> Without service endpoints, restricting access to just your VNet can be challenging.
>  The source IP address could change or could be shared with other customers.
>  For example, PaaS services with shared outbound IP addresses.
>  With service endpoints, the source IP address that the target service sees becomes a private IP address from your VNet.
>  This ingress traffic change allows for easily identifying the origin and using it for configuring appropriate firewall rules.
>  For example, allowing only traffic from a specific subnet within that VNet.
> With service endpoints, DNS entries for Azure services remain as-is and continue to resolve to public IP addresses assigned to the Azure service.

### Azure virtual network service endpoint policies
[Azure virtual network service endpoint policies](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoint-policies-overview)
is also important to be aware of in the context of Service Endpoints.
Currently it is only available for Azure Storage and provides improved security for your Virtual Network traffic to Azure Storage

[Azure service tags for network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)
 allow you to restrict virtual network outbound traffic to specific Azure Storage regions.
 However, this allows traffic to any account within selected Azure Storage region.


Endpoint policies allow you to specify the Azure Storage accounts that are allowed virtual network outbound access and restricts access to all the other storage accounts.
 This gives much more granular security control for protecting data exfiltration from your virtual network.

## Private Endpoint
[Private endpoints](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview#private-link-resource) 
allow ingress of traffic from your virtual network to an Azure resource securely.
 This private link is established without the need of public IP addresses.

*  A private endpoint is a special network interface for an Azure service in your virtual network.
*  When you create a private endpoint for your resource, it provides secure connectivity between clients on your virtual network and your Azure resource.
*  The private endpoint is assigned an IP address from the IP address range of your virtual network.
*  The connection between the private endpoint and the Azure service is a private link.
* Private endpoints provide a privately accessible IP address for the Azure service, but do not necessarily restrict public network access to it. 

See also:
* [Manage network policies for private endpoints](https://learn.microsoft.com/en-us/azure/private-link/disable-private-endpoint-network-policy?tabs=network-policy-portal)
* [Configure an application security group (ASG) with a private endpoint](https://learn.microsoft.com/en-us/azure/private-link/configure-asg-private-endpoint?tabs=portal)

## Comparing VNet Service Endpoint and Private Endpoint
It is more involved than the below, but ultimately:
* VNet Service Endpoint extends the identity of a VNet to the target service.
* Private Endpoint extends the identity of the target service to the VNet.

Put another way:
* Vnet Service Endpoint makes the VNet known to the target service.
* Private Endpoint makes the target resource known to the VNet.

[Cloud Network Security 101: Azure Service Endpoints vs. Private Endpoints](https://www.fugue.co/blog/cloud-network-security-101-azure-service-endpoints-vs.-private-endpoints)
contrasts Service Endpoint and Private Endpoint very well, but I would recommend reading everything else as well in order to understand better what is explained there.
An important point to note is that, 
if you don't need a private IP address at the destination, service endpoints are considerably easier to create and maintain, and they don't require special DNS configuration.
If you "do not need a private IP address at the destination"  may mean that 
the target resource itself  is trusted, and you need not worry about locking it down so that it cannot do anything it should not do.
If you do have a private IP address for the destination, it would imply that you have added the destination service to a subnet of a VNet, which means you can setup rules 
to restrict egress traffic from the service.


Quoting from [this answer](https://stackoverflow.com/questions/73769449/azure-difference-between-service-endpoint-and-private-endpoint-in-simple-terms)

* Private Endpoints grant network access to specific resources behind a given service providing granular segmentation. 
	- Traffic can reach the service resource from on premises without using public endpoints.

* A Service Endpoint remains a publicly routable IP address. A Private Endpoint is a private IP in the address space of the virtual network where the private endpoint is configured.

For simplicity, let's take the view of a VM in a VNET connecting to a storage account in the same subscription and same Azure region. There are three ways to connect.
1.  Default 
	- By default all traffic goes against the public endpoint of the storage account. Source IP of the traffic is the Public IP of the VM.
2.  Vnet Service Endpoints
	- Traffic is still directed against the public endpoint of the storage account but the source IP has changed to the private IP of the VM. 
	- In fact, the traffic is also using the VNET and Subnet as source in the network dataframe.
3.  Private Endpoints
	- The PaaS service now gets a virtual network interface inside the subnet and traffic from the VM to the storage account is now directed against the private IP address.

See also [Difference between Private Endpoint and Service Endpoint](https://the-tech-guy.in/2022/04/23/private-endpoint-vs-service-endpoint/)

## Private IP Addresses
[Private IP Addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/private-ip-addresses)
gives important information on how Azure assigns IP addresses dynamically inside a VNet.
* Private IP addresses are assigned sequentially from the address space of the subnet.
* First 4 addresses and last address is not avaiable (10.0.0.0/16 subnet would have 10.0.0.0 through 10.0.0.3, and 10.0.255.255 reserved).
* Default allocation method is dynamic (other method is static).
* Once assigned, dynamic IP addresses are released if a network interface is:
	- Deleted
	- Reassigned to a different subnet within the same virtual network.
	- The allocation method is changed to static, and a different IP address is specified.
* By default, Azure assigns the previous dynamically assigned address as the static address when you change the allocation method from dynamic to static.
* To assign the network interface to a different subnet, you 
	- change the allocation method from static to dynamic.
	-  Assign the network interface to a different subnet, then change the allocation method back to static.
	-  Assign an IP address from the new subnet's address range.

See also 
[Azure Resource Limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits?toc=%2Fazure%2Fvirtual-network%2Ftoc.json#networking-limits)

## Implementations

* [Setting Service Endpoints via Terraform](https://blog.nillsf.com/index.php/2020/10/14/using-terraform-to-create-vnet-service-endpoints/)
* [Azure Private Endpoints and Terraform](https://jeffreyjblanchard.medium.com/azure-private-endpoints-and-terraform-85450fe9861c)
* [Using Private Endpoint in Azure Storage Account with Terraform](https://gmusumeci.medium.com/using-private-endpoint-in-azure-storage-account-with-terraform-49b4734ada34)
* [Private Endpoints with Terraform](https://jfarrell.net/2021/07/03/private-endpoints-with-terraform/)
* [Using Terraform to create Private Endpoint for Azure Database for MariaDB](https://techcommunity.microsoft.com/t5/azure-database-for-mysql-blog/using-terraform-to-create-private-endpoint-for-azure-database/ba-p/1279947)

