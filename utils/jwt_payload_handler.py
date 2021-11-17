#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/11/17 19:47 
# email： liang1.li@ximalaya.com

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user_id':user.id,
        'user_name':user.username
    }