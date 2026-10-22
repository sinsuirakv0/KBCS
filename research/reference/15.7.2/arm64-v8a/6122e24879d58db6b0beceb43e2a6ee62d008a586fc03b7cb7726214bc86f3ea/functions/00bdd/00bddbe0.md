# 00bddbe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bddbe0.md)

## 関数情報

~~~json
{
  "address": "00bddbe0",
  "name": "firebase::remote_config::RemoteConfig::GetInstance",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "60294f5e043008c12e04209d24f191d2ace0831c3673ef183bc04b62c3b923ca",
  "source_text_sha256": "60294f5e043008c12e04209d24f191d2ace0831c3673ef183bc04b62c3b923ca"
}
~~~
## 呼び出し元

- [0084b5fc](../0084b/0084b5fc.md)

## 呼び出し先

- [00b524b4](../00b52/00b524b4.md)

## 疑似コード 1/1 / UTF-8 136 bytes

~~~c

void firebase::remote_config::RemoteConfig::GetInstance(App *param_1)

{
  (*(code *)PTR_GetInstance_00c1d628)();
  return;
}

~~~
