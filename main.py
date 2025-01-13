import base64
import urllib.parse


def parse_url_encoded_string(url_encoded_string):
    print("original: ", url_encoded_string)

    url_decoded_string = urllib.parse.unquote(url_encoded_string)
    print("url_decoded_string: ", url_decoded_string)

    decoded_bytes = base64.b64decode(url_decoded_string)
    try:
        decoded_str = decoded_bytes.decode('utf-8')
        print("decoded_str: ", decoded_str)
    except Exception as e:
        print("error: ", e)
        byte_values = list(decoded_bytes)
        print("byte_values: ", byte_values)
    
    print("decoded_bytes: ", decoded_bytes)
    byte_values = list(decoded_bytes)
    print("byte_values: ", byte_values)


parse_url_encoded_string("05IAvI0RcleF41tLr6SPluE2rDwEK60XTVi0nTT/gZN5+A88Ir2Aca03z5WtMTlPB8JG0ycewEGweyQVxNavNiYys1phrWXOEQcBG4zyCqTB8oqR2rMAQM7AqkT8vgN/xDvYLJX+VlprjZKqAeEgmvQMchzHJoPnmDNW2SOPmmE=")




