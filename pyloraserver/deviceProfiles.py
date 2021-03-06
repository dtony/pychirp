class DeviceProfiles:
    """
    A class representing Device Profiles within LoRaServer.io

    Args:
        name (str): The name of the device profile.
        description (str): A description of the device profile.
        loraserver_connection (loraserver_connection):
            A loraserver_connection object
    Returns:
        DeviceProfiles: A device profile object
    """

    def __init__(self,
                 name=None,
                 description=None,
                 loraserver_connection=None
                 ):
        self.lscx = loraserver_connection

    def list(self,
             limit=10,
             offset=0,
             appid=None,
             orgid=None):
        """
        Get a list of all of the device profiles

        Args:
            limit (int): The number of results to return (must be more than 0)
            offset (int): The results offset for pagination purposes
            search_term (str): Text to search for in the device profile name
            appid (int): The application to restrict the search to
            orgid (int): The organisation to restrict the search to
        Returns:
            dict: A dict of the search results
        """
        url = "%s/api/device-profiles?limit=%s&offset=%s" % (
                self.lscx.loraserver_url,
                limit,
                offset)
        if appid is not None:
            url = "%s&applicationID=%s" % (url, appid)
        if orgid is not None:
            url = "%s&organizationID=%s" % (url, orgid)

        ret_list = self.lscx.connection.get(url)
        return ret_list.json()
