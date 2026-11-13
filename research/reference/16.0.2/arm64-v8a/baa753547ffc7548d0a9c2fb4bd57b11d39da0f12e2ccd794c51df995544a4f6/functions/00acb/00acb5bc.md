# 00acb5bc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00acb5bc",
  "name": "FUN_00acb5bc",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd0e0a7b69894b5ecb65515f7850890b1551c75360e91d754865fd6689846a07",
  "source_text_sha256": "fd0e0a7b69894b5ecb65515f7850890b1551c75360e91d754865fd6689846a07"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [0047d1fc](../0047d/0047d1fc.md)
- [00851550](../00851/00851550.md)
- [00b3bf30](../00b3b/00b3bf30.md)

## 疑似コード / UTF-8 1676 bytes

~~~c

void FUN_00acb5bc(undefined8 param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  undefined8 uVar4;
  
  iVar1 = *param_3;
  if (iVar1 != 4) {
    if (iVar1 == 3) {
      uVar2 = FUN_0047ad34();
      uVar4 = 0xb;
    }
    else {
      if (iVar1 != 0) {
        return;
      }
      uVar2 = FUN_0047ad34();
      uVar4 = 10;
    }
    FUN_0047ce14(uVar2,uVar4,0);
    return;
  }
  lVar3 = FUN_00851550();
  iVar1 = *(int *)(lVar3 + 0x4a818);
  lVar3 = FUN_00851550();
  if (iVar1 != 0) {
    iVar1 = FUN_00b3bf30(lVar3 + 0xc400);
    lVar3 = FUN_00851550();
    if (iVar1 < 900000) {
      *(undefined4 *)(lVar3 + 0x3478) = 0;
      lVar3 = FUN_00851550();
      *(undefined1 *)(lVar3 + 0x3480) = 1;
    }
    else {
      *(undefined1 *)((long)&fde_table_entry_00335f18.initial_loc + lVar3 + 2) = 1;
      lVar3 = FUN_00851550();
      *(undefined4 *)((long)&fde_table_entry_00335f30.data_loc + lVar3) = 10000;
    }
    return;
  }
  *(undefined4 *)(lVar3 + 0x4a818) = 1;
  lVar3 = FUN_00851550();
  *(undefined1 *)((long)&fde_table_entry_00336f50.data_loc + lVar3) = 1;
  FUN_00851550();
  lVar3 = FUN_00851550();
  *(undefined4 *)((long)&fde_table_entry_00336f58.initial_loc + lVar3) = 0;
  FUN_00851550();
  lVar3 = FUN_00851550();
  *(undefined4 *)((long)&fde_table_entry_00336f58.data_loc + lVar3) = 0;
  FUN_00851550();
  lVar3 = FUN_00851550();
  *(undefined4 *)((long)&fde_table_entry_00336f60.initial_loc + lVar3) = 0;
  FUN_00851550();
  lVar3 = FUN_00851550();
  *(undefined4 *)((long)&fde_table_entry_00336f60.data_loc + lVar3) = 0;
  FUN_00851550();
  uVar2 = FUN_0047ad34();
  FUN_0047d1fc(uVar2,0x32);
  return;
}

~~~
