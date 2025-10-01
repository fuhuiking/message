from typing import List, Optional
from pydantic import BaseModel 

# 输入参数
class EnterpriseItem(BaseModel):
    """单个企业信息条目（对应列表中的一项）"""
    # 对应：企业简称
    enterprise_abbreviation: str
    # 对应：企业全称
    enterprise_full_name: str
    # 对应：企业分类
    enterprise_category: str

class EnterpriseDict(BaseModel):
    """企业信息字典（包含企业列表的顶层结构）"""
    enterprise_info_list: List[EnterpriseItem]

class CategoryItem(BaseModel):
    """单个投诉类别条目（对应列表中的一项）"""
    # 对应：类别名称
    category_name: str
    # 对应：类别定义描述
    category_definition: str
    # 对应：案例例子
    case_examples: List[str]

class CategoryDict(BaseModel):
    """投诉类别字典"""
    # 对应：违规类型——信访-保险
    violation_type_petition_insurance: List[CategoryItem]
    # 对应：违规类型——信访-银行
    violation_type_petition_bank: List[CategoryItem]
    # 对应：主要违规问题——分类信息-信访-银行
    major_violation_issue_classification_petition_bank: List[CategoryItem]
    # 对应：主要违规问题——分类信息-信访-保险
    major_violation_issue_classification_petition_insurance: List[CategoryItem]
    # 对应：违规类型（年报统计）——分类信息-信访-银行
    violation_type_annual_report_classification_petition_bank: List[CategoryItem]
    # 对应：违规类型（年报统计）——分类信息-信访-保险
    violation_type_annual_report_classification_petition_insurance: List[CategoryItem]
    # 对应：销售渠道（保单渠道）——分类信息-信访-银行
    sales_channel_policy_classification_petition_bank: List[CategoryItem]


class ComplaintRequest(BaseModel):
    """投诉信访请求参数（完整输入结构）"""
    data: str
    task_id: str


# 输出参数
class ComplainedObject(BaseModel):
    """投诉对象信息"""
    complaintObjectName: str
    deptName: str
    content: str

class PetitionClassificationInfo(BaseModel):
    """信访分类信息"""
    violationType: str
    violationQuestion: str
    violationTypeStatistics: str
    businessType: str
    complaintReason: str
    disputeType: str
    demandContent: str

class Result(BaseModel):
    """result字段的具体结构（包含两个子对象）"""
    complainedObject: ComplainedObject
    petitionClassificationInfo: PetitionClassificationInfo

class ApiStatus(BaseModel):
    """接口状态信息"""
    code: str
    message: str

class ComplaintResponse(BaseModel):
    """投诉信访响应结果（result类型）"""
    status: ApiStatus
    result: Optional[Result]
