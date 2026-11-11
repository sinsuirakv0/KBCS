# 00c2dfbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00c2dfbc",
  "name": "FUN_00c2dfbc",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ddeec2dbe61d8aff306e20858b27f44c22af314cbd8a75a2055deae19101c84f",
  "source_text_sha256": "ddeec2dbe61d8aff306e20858b27f44c22af314cbd8a75a2055deae19101c84f"
}
~~~

## 呼び出し元

- [00c2df50](../00c2d/00c2df50.md)

## 呼び出し先

- [00c57e30](../00c57/00c57e30.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)

## 疑似コード / UTF-8 873 bytes

~~~c

void FUN_00c2dfbc(void)

{
  int iVar1;
  undefined2 *puVar2;
  
  if (((DAT_01128718 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01128718), iVar1 != 0)) {
    __cxa_atexit(FUN_00c35f20,0,&PTR_LOOP_00c62f90);
    __cxa_guard_release(&DAT_01128718);
  }
  if ((DAT_011286e8 & 1) == 0) {
    DAT_011286e8 = 4;
    puVar2 = &DAT_011286e9;
  }
  else {
    DAT_011286f0 = 2;
    puVar2 = DAT_011286f8;
  }
  *(undefined1 *)(puVar2 + 1) = 0;
  *puVar2 = 0x4d41;
                    /* try { // try from 00c2e020 to 00d2e03b has its CatchHandler @ 00c2e474 */
  if ((DAT_01128700 & 1) == 0) {
    DAT_01128700 = 4;
    puVar2 = &DAT_01128701;
  }
  else {
                    /* try { // try from 00c2e03c to 00d2e117 has its CatchHandler @ 00c2dce0 */
    DAT_01128708 = 2;
    puVar2 = DAT_01128710;
  }
  *puVar2 = 0x4d50;
  *(undefined1 *)(puVar2 + 1) = 0;
  return;
}

~~~
