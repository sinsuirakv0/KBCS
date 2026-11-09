# 00b3aecc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b3aecc",
  "name": "FUN_00b3aecc",
  "size": 220,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1295c6866fdc571deadc25eac4126a8c56105f08bafabed28aaf90ff60069162",
  "source_text_sha256": "1295c6866fdc571deadc25eac4126a8c56105f08bafabed28aaf90ff60069162"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 1586 bytes

~~~c

void FUN_00b3aecc(undefined8 *param_1,undefined8 param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  void *__ptr;
  
  __ptr = (void *)*param_1;
  *param_1 = param_2;
  if (__ptr == (void *)0x0) {
    return;
  }
  if (*(char *)(param_1 + 2) == '\0') goto LAB_00b3af98;
  plVar1 = *(long **)((long)__ptr + 0xc0);
  plVar3 = (long *)((long)__ptr + 0xa0);
  if (plVar1 == plVar3) {
    lVar4 = 0x20;
LAB_00b3af1c:
    (**(code **)(*plVar3 + lVar4))();
  }
  else if (plVar1 != (long *)0x0) {
    lVar4 = 0x28;
    plVar3 = plVar1;
    goto LAB_00b3af1c;
  }
  plVar2 = *(long **)((long)__ptr + 0x90);
  plVar3 = (long *)((long)__ptr + 0x70);
  plVar1 = (long *)((long)__ptr + 0x40);
                    /* try { // try from 00b3af34 to 00c3af3b has its CatchHandler @ 00b3b60c */
  if (plVar2 == plVar3) {
    lVar4 = 0x20;
LAB_00b3af50:
    (**(code **)(*plVar3 + lVar4))();
  }
  else if (plVar2 != (long *)0x0) {
    lVar4 = 0x28;
    plVar3 = plVar2;
    goto LAB_00b3af50;
  }
  plVar3 = *(long **)((long)__ptr + 0x60);
  if (plVar3 == plVar1) {
    lVar4 = 0x20;
LAB_00b3af7c:
                    /* try { // try from 00b3af84 to 00c3af97 has its CatchHandler @ 00b3b5d8 */
    (**(code **)(*plVar1 + lVar4))();
  }
  else if (plVar3 != (long *)0x0) {
                    /* try { // try from 00b3af6c to 00c3af83 has its CatchHandler @ 00b3b5f0 */
    lVar4 = 0x28;
    plVar1 = plVar3;
    goto LAB_00b3af7c;
  }
  if ((*(byte *)((long)__ptr + 0x20) & 1) != 0) {
    _ZdlPv(*(void **)((long)__ptr + 0x30));
  }
LAB_00b3af98:
  _ZdlPv(__ptr);
  return;
}

~~~
