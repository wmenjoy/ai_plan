# AI工具使用监控脚本
def analyze_usage(logs):
    """
    分析指标：
    - 生成代码采纳率
    - 平均响应时间
    - 安全事件发生率
    """
    metrics = {
        'adoption_rate': len([l for l in logs if l['used']])/len(logs),
        'avg_response': np.mean([l['latency'] for l in logs]),
        'security_incidents': sum(1 for l in logs if l['risk_level'] > 3)
    }
    return metrics 