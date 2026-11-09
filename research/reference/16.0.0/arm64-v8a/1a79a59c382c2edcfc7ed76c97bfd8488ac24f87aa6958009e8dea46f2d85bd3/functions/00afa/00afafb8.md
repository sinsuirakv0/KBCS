# 00afafb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00afafb8",
  "name": "FUN_00afafb8",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "68a43de458a730a6f8cef2357cafa3f0a71283520c6b1c824fb13b312cb5fb10",
  "source_text_sha256": "68a43de458a730a6f8cef2357cafa3f0a71283520c6b1c824fb13b312cb5fb10"
}
~~~

## 呼び出し元

- [0070ea1c](../0070e/0070ea1c.md)
- [007119b0](../00711/007119b0.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 377 bytes

~~~c

bool FUN_00afafb8(int param_1,int param_2)

{
  long lVar1;
  
                    /* try { // try from 00afafc0 to 00bfafe3 has its CatchHandler @ 00afb164 */
  lVar1 = FUN_008514b8();
                    /* try { // try from 00afafe4 to 00bfb2af has its CatchHandler @ 00afaa30 */
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c54) != 0;
}

~~~
