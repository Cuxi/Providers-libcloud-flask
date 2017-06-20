def resize_node(self, size, idNode):
        """
        Create a node.

        The `ex_create_attr` parameter can include the following dictionary
        key and value pairs:

        * `backups`: ``bool`` defaults to False
        * `ipv6`: ``bool`` defaults to False
        * `private_networking`: ``bool`` defaults to False
        * `user_data`: ``str`` for cloud-config data
        * `ssh_keys`: ``list`` of ``int`` key ids or ``str`` fingerprints

        `ex_create_attr['ssh_keys']` will override `ex_ssh_key_ids` assignment.

        :keyword ex_create_attr: A dictionary of optional attributes for
                                 droplet creation
        :type ex_create_attr: ``dict``

        :keyword ex_ssh_key_ids: A list of ssh key ids which will be added
                                 to the server. (optional)
        :type ex_ssh_key_ids: ``list`` of ``int`` key ids or ``str``
                              key fingerprints

        :keyword    ex_user_data:  User data to be added to the node on create.
                                     (optional)
        :type       ex_user_data:  ``str``

        :return: The newly created node.
        :rtype: :class:`Node`
        """
        attr = {'type': 'resize', 'size': size.name}


        res = self.connection.request('/v2/droplets/%s/actions' % (idNode.id),
                                      data=json.dumps(attr), method='POST')

        data = res.object['action']
        # TODO: Handle this in the response class
        status = res.object.get('status', 'completed' or 'in-progress')
        statusFailed = res.object.get('status', 'errored')

        if status == 'errored':
            return statusFailed

        if status == 'None':
            return statusFailed

        if status == 'ERROR':
            return statusFailed

        return status