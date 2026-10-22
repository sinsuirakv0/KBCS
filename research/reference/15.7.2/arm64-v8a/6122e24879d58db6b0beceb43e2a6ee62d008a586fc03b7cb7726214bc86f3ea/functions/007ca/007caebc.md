# 007caebc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007caebc.md)

## 関数情報

~~~json
{
  "address": "007caebc",
  "name": "operator.delete",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d689b86c8bc59e1ee4d74f5170198c2dec03496219c31e34578faf85295e02eb",
  "source_text_sha256": "d689b86c8bc59e1ee4d74f5170198c2dec03496219c31e34578faf85295e02eb"
}
~~~
## 呼び出し元

- [0079bdf0](../0079b/0079bdf0.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 204 bytes

~~~c

void operator_delete(void *param_1)

{
                    /* try { // try from 007caebc to 008caec7 has its CatchHandler @ 007ce094 */
  (*(code *)PTR_operator_delete_00c1bfe8)();
  return;
}

~~~
