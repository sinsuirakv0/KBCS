# 00bda6cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bda6cc.md)

## 関数情報

~~~json
{
  "address": "00bda6cc",
  "name": "FUN_00bda6cc",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0245f82b1bd69854ee866af1380dc8c63235fb86fe602907fe8b360b5fe1defb",
  "source_text_sha256": "0245f82b1bd69854ee866af1380dc8c63235fb86fe602907fe8b360b5fe1defb"
}
~~~
## 呼び出し元

- [00bda59c](../00bda/00bda59c.md)
- [00bda9b4](../00bda/00bda9b4.md)

## 呼び出し先

- [00bd93b0](../00bd9/00bd93b0.md)
- [00bdd260](../00bdd/00bdd260.md)
- [00be1e80](../00be1/00be1e80.md)

## 関連文字列（未確認候補）

~~~text
"libunwind: unsupported .eh_frame_hdr at %lx: need at least 4 bytes of data but only got %zd\n"
"libunwind: unsupported .eh_frame_hdr version: %u at %lx\n"
~~~
## 疑似コード 1/1 / UTF-8 1441 bytes

~~~c

undefined8 FUN_00bda6cc(undefined8 param_1,byte *param_2,byte *param_3,undefined8 *param_4)

{
  byte bVar1;
  byte bVar2;
  undefined *puVar3;
  undefined8 uVar4;
  byte *local_28;
  
  puVar3 = PTR___sF_00c1bc48;
  if ((ulong)((long)param_3 - (long)param_2) < 4) {
    if (param_3 == param_2) {
      return 0;
    }
    fprintf((FILE *)(PTR___sF_00c1bc48 + 0x130),
            "libunwind: unsupported .eh_frame_hdr at %lx: need at least 4 bytes of data but only got %zd\n"
            ,param_2);
  }
  else {
                    /* try { // try from 00bda720 to 00cda72f has its CatchHandler @ 00bda82c */
    if (*param_2 == 1) {
      local_28 = param_2 + 4;
                    /* try { // try from 00bda730 to 00cda86b has its CatchHandler @ 00bda6ac */
      bVar1 = param_2[2];
      bVar2 = param_2[1];
      *(byte *)(param_4 + 3) = param_2[3];
      uVar4 = FUN_00bd93b0(param_1,&local_28,param_3,bVar2,param_2);
      *param_4 = uVar4;
      if (bVar1 == 0xff) {
        uVar4 = 0;
      }
      else {
        uVar4 = FUN_00bd93b0(param_1,&local_28,param_3,bVar1,param_2);
      }
      param_4[1] = uVar4;
      param_4[2] = local_28;
      return 1;
    }
    fprintf((FILE *)(PTR___sF_00c1bc48 + 0x130),
            "libunwind: unsupported .eh_frame_hdr version: %u at %lx\n",(ulong)(uint)*param_2,
            param_2);
  }
  fflush((FILE *)(puVar3 + 0x130));
  return 0;
}

~~~
