# 说明
本文档为测试用例yaml编写的说明文档

## 用例说明

用例分为三部分

- ```testinfo``` 表示用例介绍
    - ```id``` 用例id
    - ```title``` 用例标题
    - ```info``` 前置条件
- ```testcase``` 用例的执行步骤
    - ```element_info: com.huawei.works.contact:id/title``` 元素
    - ```find_type: id```  元素类型
        - ```id```
        - ```xpath```
        - ```css```
        - ```ids```
            - ```index```
    - ```operate_type: click``` 操作
        - ```click```
        - ```swipe_down```
        - ```swipe_up```
        - ```swipe_to_left```  以选中的元素为所标左滑
        - ```swipe_left```  选中当前元素左滑
        - ```get_value```
        - ```set_value``` 
            - ```msg``` 传给```set_value```关键字
        - ```adb_tab``` 使用adb中的tab命令点击元素,元素必须可识别，应用于悬浮层场景
        - ``` long_time``` 长按
        - ```get_content_desc``` 无法切换到webview时，用此关键字
        - ```press_key_code``` 键盘触发事件，需要传```code```
            - ```code``` 传给```press_key_code```关键字
        - ```is_webview:1``` 为1表示切换到webview,为2表示切换到原生
        - ```is_checked``` 用于判断元素是否被选中
        - ```is_selected``` 用户判断表格元素是否被选中
    - ```is_time: 3``` 自定义暂停3秒
    - ```info: 点击动态列表第一条数据``` 操作步骤介绍
- ```check``` 检查点,支持多检查点
    - ```element_info: com.huawei.works.knowledge:id/browser_knowledge_history_text``` 元素
    - ```find_type: ids``` 元素类型，同testcase
        - ```index: 0``` 当元素类型为ids时，支持
    - ```operate_type: get_value``` 操作类型，，同testcase
    - ```checking``` 检查方式
        - ```default_check``` 默认检查点，元素存在，操作正常用例通过
        - ```contrary```  相反检查点，如果元素存在说明失败。比如删除操作
        - ```contrary_getval``` 相反值检查点，值对比失败用例成功
        - ```compare``` 历史数据与实际数据对比
        - ```contain``` 实际数据包含历史数据
        - ```toast``` 获取toast元素
    - ```info: 查找是否存在历史记录```