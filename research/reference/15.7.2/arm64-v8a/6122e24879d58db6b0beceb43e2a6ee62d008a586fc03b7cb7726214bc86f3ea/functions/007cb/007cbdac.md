# 007cbdac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007cbdac.md)

## 関数情報

~~~json
{
  "address": "007cbdac",
  "name": "FUN_007cbdac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "780f5d107282b9a1d007044b1e0e331fab219ddee84e9a38bf31d0959dca4fa0",
  "source_text_sha256": "780f5d107282b9a1d007044b1e0e331fab219ddee84e9a38bf31d0959dca4fa0"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード 1/1 / UTF-8 369 bytes

~~~c

void FUN_007cbdac(undefined8 *param_1)

{
  void *pvVar1;
  
  pvVar1 = (void *)param_1[2];
  *param_1 = &PTR_FUN_00bffef8;
  if (pvVar1 != (void *)0x0) {
    param_1[3] = pvVar1;
    operator_delete(pvVar1);
  }
                    /* try { // try from 007cbde8 to 008cbe0f has its CatchHandler @ 007cde44 */
  operator_delete(param_1);
  return;
}

~~~
