# Copyright 2019 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Configuration File

#pins configuration
device_config = {
  'led_pin': 1,
  'scl_pin': 22,
  'sda_pin': 21,
  'sleeptime':10
}

#delay between sensrors readings

wifi_config = {
    'ssid':'YOUR ESSID',
    'password':'YOUR PASSWORD'
}

google_cloud_config = {
    'project_id':'',
    'cloud_region':'',
    'registry_id':'',
    'device_id':'',
    'mqtt_bridge_hostname':'mqtt.googleapis.com',
    'mqtt_bridge_port':8883
}

jwt_config = {
    'algorithm':'RS256',
    'token_ttl': 43200, #12 hours
    # Use utiles/decode_rsa.py to decode private pem to pkcs1.
    'private_key':()
}

