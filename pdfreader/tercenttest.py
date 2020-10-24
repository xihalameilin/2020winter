import base64
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models


# TextTable
# 表格识别结果
#
# 被如下接口引用：TableOCR。
#
# 名称	类型	描述
# ColTl	Integer	单元格左上角的列索引
# RowTl	Integer	单元格左上角的行索引
# ColBr	Integer	单元格右下角的列索引
# RowBr	Integer	单元格右下角的行索引
# Text	String	单元格文字
# Type	String	单元格类型，包含body（表格主体）、header（表头）、footer（表尾）三种
# Confidence	Integer	置信度 0 ~100
# Polygon	Array of Coord	文本行坐标，以四个顶点坐标表示
# AdvancedInfo	String	此字段为扩展字段


# 参数名称 类型 描述
# TextDetections Array of TextTable 检测到的文本信息，具体内容请点击左侧链接。
# Data String Base64 编码后的 Excel 数据。
# RequestId String 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。

def imgget(path):
    with open(path, "rb") as f:#转为二进制格式
        base64_data = base64.b64encode(f.read())#使用base64进行加密
    return base64_data.decode('utf-8')

# #print(resp.Data) #Base64 编码后的 Excel 数据
# data = base64.b64decode(resp.Data)
#文件保存函数
def save(data, name):
    path = name
    with open(path, "wb")as f:
        f.write(data)
    f.close



try:
    cred = credential.Credential("AKIDWo33mJWaJlfbJjFkhZ6PULVP2bv2FQkK", "hA2g2830h7GUA3f0XUDk3JOERIsKXUpy")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-shanghai", clientProfile)

    req = models.TableOCRRequest()

    params = imgget("22.png")
    req.ImageBase64 = str(params)
    # req.from_json_string(params)

    resp = client.TableOCR(req)
    print(resp)
    print(resp.to_json_string())
    data = base64.b64decode(resp.Data)
    name = '腾讯云表格识别结果3.xlsx'
    save(data, name)

except TencentCloudSDKException as err:
    print(err)


