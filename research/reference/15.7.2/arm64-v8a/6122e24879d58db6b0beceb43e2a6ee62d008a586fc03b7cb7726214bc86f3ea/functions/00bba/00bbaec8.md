# 00bbaec8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00bbaec8",
  "name": "_ZNSt12length_errorD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ef0227429fdf6497c07f5e10f12261b19e26deb569805575c4e512b52863ee6a",
  "source_text_sha256": "ef0227429fdf6497c07f5e10f12261b19e26deb569805575c4e512b52863ee6a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdafb0](../00bda/00bdafb0.md)

## 疑似コード / UTF-8 302 bytes

~~~c

void _ZNSt12length_errorD0Ev(void *param_1)

{
  _ZNSt11logic_errorD1Ev();
                    /* try { // try from 00bbaee4 to 00cbaeef has its CatchHandler @ 00bbb7c8 */
                    /* try { // try from 00bbaef0 to 00cbaeff has its CatchHandler @ 00bbb790 */
  _ZdlPv(param_1);
  return;
}

~~~
