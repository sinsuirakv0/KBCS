# 00bcbac4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bcbac4.md)

## 関数情報

~~~json
{
  "address": "00bcbac4",
  "name": "FUN_00bcbac4",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "18bf49f8154c85981da466cb02e34c046ec0ec8fc0e1335cbb8ff428030c944d",
  "source_text_sha256": "18bf49f8154c85981da466cb02e34c046ec0ec8fc0e1335cbb8ff428030c944d"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 疑似コード 1/1 / UTF-8 1099 bytes

~~~c

void FUN_00bcbac4(long param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  ulong uVar2;
  void *__ptr;
  long lVar3;
  size_t __size;
  
  (**(code **)(**(long **)(param_1 + 0x18) + 0x20))();
  puVar1 = *(undefined8 **)(param_1 + 0x18);
  if ((*(byte *)((long)puVar1 + 9) & 0xc0) == 0x80) {
    uVar2 = (**(code **)*puVar1)(puVar1,param_2);
    if ((uVar2 & 1) != 0) {
      return;
    }
  }
  else if (*(byte *)((long)puVar1 + 9) < 0x40) {
    return;
  }
                    /* try { // try from 00bcbb20 to 00ccbc43 has its CatchHandler @ 00bcba3c */
  lVar3 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 1U) {
    __size = param_2[2] * 2;
    uVar2 = lVar3 + 0x3e1;
    if (__size < uVar2 || __size - uVar2 == 0) {
      __size = uVar2;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
  *(undefined1 *)((long)__ptr + lVar3) = 0x20;
  param_2[1] = param_2[1] + 1;
  return;
}

~~~
