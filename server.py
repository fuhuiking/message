from fastapi import FastAPI
from schemal import ComplaintRequest, ComplaintResponse, ApiStatus, Result
import logging
from logging.handlers import RotatingFileHandler

# 初始化日志，保存到 server.log 文件，50MB 大小，保留 100 个备份
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler("./output/server.log", maxBytes=50*1024*1024, backupCount=100, encoding='utf-8'),
        logging.StreamHandler()  # 同时输出到控制台
    ]
)

app = FastAPI(
    title="Complaint & Petition API",
    description="API for complaint/petition data with dict-list nested structure",
    version="1.0.0"
)

@app.post("/v1/process", response_model=ComplaintResponse)
async def process_complaint(request: ComplaintRequest):
    logging.info(f"Received request: task_id({request.task_id}), content({request.data[:50]}...)")

    # 这里可以添加实际的处理逻辑，目前返回示例数据
    #result = extract_complaint_info(request)

    #debug log the result
    result = Result(
        complainedObject={
            "complaintObjectName": "示例投诉对象",
            "deptName": "示例部门",
            "content": "这是一个示例投诉内容"
        },
        petitionClassificationInfo={
            "violationType": "示例违规类型",
            "violationQuestion": "示例违规问题",
            "violationTypeStatistics": "示例违规类型统计",
            "businessType": "示例业务类型",
            "complaintReason": "示例投诉原因",
            "disputeType": "示例争议类型",
            "demandContent": "示例诉求内容"
        }
    )

    return ComplaintResponse(
        status=ApiStatus(code='200', message="SUCCESS"),
        result=result
    )
@app.get("/", include_in_schema=False)
async def root():
    return {"message": "API running", "docs": "/docs"}