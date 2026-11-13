# 00abd8dc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00abd8dc",
  "name": "FUN_00abd8dc",
  "size": 128,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4919b99bf919285e2ca2760a2df4a3b319bf8d1f3af141088d37c3628866f8fc",
  "source_text_sha256": "4919b99bf919285e2ca2760a2df4a3b319bf8d1f3af141088d37c3628866f8fc"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0086a244](../0086a/0086a244.md)
- [00c57f80](../00c57/00c57f80.md)

## 疑似コード / UTF-8 615 bytes

~~~c

void FUN_00abd8dc(undefined8 *param_1)

{
  long *__ptr;
  long lVar1;
  long *plVar2;
  long *plVar3;
  
                    /* try { // try from 00abd8e4 to 00bbd963 has its CatchHandler @ 00abd840 */
  plVar3 = (long *)*param_1;
  if (plVar3 == (long *)0x0) {
    return;
  }
  plVar2 = (long *)param_1[1];
  __ptr = plVar3;
  if (plVar2 != plVar3) {
    do {
      plVar2 = plVar2 + -1;
      lVar1 = *plVar2;
      *plVar2 = 0;
      if (lVar1 != 0) {
        FUN_0086a244(plVar2);
      }
    } while (plVar2 != plVar3);
    __ptr = (long *)*param_1;
  }
  param_1[1] = plVar3;
  _ZdlPv(__ptr);
  return;
}

~~~
