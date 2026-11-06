# 00bdaff0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bdaff0.md)

## 関数情報

~~~json
{
  "address": "00bdaff0",
  "name": "<EXTERNAL>::__register_atfork",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "097c888f1382fc1ba10f6d8f4dab5e20f04ef0b3ef7a08a4dcc4df0014984a78",
  "source_text_sha256": "097c888f1382fc1ba10f6d8f4dab5e20f04ef0b3ef7a08a4dcc4df0014984a78"
}
~~~
## 呼び出し元

- [00418320](../00418/00418320.md)

## 呼び出し先

- [010a5010](../010a5/010a5010.md)

## 疑似コード 1/1 / UTF-8 190 bytes

~~~c

void __register_atfork(void)

{
                    /* try { // try from 00bdaff8 to 00cdb057 has its CatchHandler @ 00bdaf98 */
  (*(code *)PTR___register_atfork_00c1c0b0)();
  return;
}

~~~
