# 00bda7cc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bda7cc",
  "name": "FUN_00bda7cc",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fb537be12c93e6f6005184c61fcbb88f9102fa346cf5f4bfe6a4f9f74fa2d20e",
  "source_text_sha256": "fb537be12c93e6f6005184c61fcbb88f9102fa346cf5f4bfe6a4f9f74fa2d20e"
}
~~~

## 呼び出し元

- [00bda69c](../00bda/00bda69c.md)
- [00bdaab4](../00bda/00bdaab4.md)

## 呼び出し先

- [00bd94b0](../00bd9/00bd94b0.md)
- [00bdd360](../00bdd/00bdd360.md)
- [00be1f80](../00be1/00be1f80.md)

## 関連文字列（未確認候補）

~~~text
"libunwind: unsupported .eh_frame_hdr at %lx: need at least 4 bytes of data but only got %zd\n"
"libunwind: unsupported .eh_frame_hdr version: %u at %lx\n"
~~~

## 疑似コード / UTF-8 1394 bytes

~~~c

undefined8 FUN_00bda7cc(undefined8 param_1,byte *param_2,byte *param_3,undefined8 *param_4)

{
  byte bVar1;
  byte bVar2;
  undefined *puVar3;
  undefined8 uVar4;
  byte *local_28;
  
  puVar3 = PTR___sF_00c1bd48;
  if ((ulong)((long)param_3 - (long)param_2) < 4) {
    if (param_3 == param_2) {
      return 0;
    }
    fprintf((FILE *)(PTR___sF_00c1bd48 + 0x130),
            "libunwind: unsupported .eh_frame_hdr at %lx: need at least 4 bytes of data but only got %zd\n"
            ,param_2);
  }
  else {
    if (*param_2 == 1) {
                    /* try { // try from 00bda82c to 00cda83b has its CatchHandler @ 00bda938 */
      local_28 = param_2 + 4;
      bVar1 = param_2[2];
      bVar2 = param_2[1];
                    /* try { // try from 00bda83c to 00cda977 has its CatchHandler @ 00bda7b8 */
      *(byte *)(param_4 + 3) = param_2[3];
      uVar4 = FUN_00bd94b0(param_1,&local_28,param_3,bVar2,param_2);
      *param_4 = uVar4;
      if (bVar1 == 0xff) {
        uVar4 = 0;
      }
      else {
        uVar4 = FUN_00bd94b0(param_1,&local_28,param_3,bVar1,param_2);
      }
      param_4[1] = uVar4;
      param_4[2] = local_28;
      return 1;
    }
    fprintf((FILE *)(PTR___sF_00c1bd48 + 0x130),
            "libunwind: unsupported .eh_frame_hdr version: %u at %lx\n",(ulong)(uint)*param_2,
            param_2);
  }
  fflush((FILE *)(puVar3 + 0x130));
  return 0;
}

~~~
