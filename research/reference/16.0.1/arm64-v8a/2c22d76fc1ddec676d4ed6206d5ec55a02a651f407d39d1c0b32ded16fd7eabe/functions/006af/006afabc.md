# 006afabc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "006afabc",
  "name": "FUN_006afabc",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3e16be73fe160c32e20a1a33b68d4337e5f8a1e70af9b867adfd42ee2877dd00",
  "source_text_sha256": "3e16be73fe160c32e20a1a33b68d4337e5f8a1e70af9b867adfd42ee2877dd00"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [006a6a54](../006a6/006a6a54.md)
- [00811368](../00811/00811368.md)
- [00ab09f4](../00ab0/00ab09f4.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 1427 bytes

~~~c

void FUN_006afabc(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  long lVar5;
  undefined8 local_58;
  undefined8 uStack_50;
  undefined8 local_48;
  undefined8 uStack_40;
  long local_38;
  
                    /* try { // try from 006afac4 to 007afc77 has its CatchHandler @ 006af8e8 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lVar5 = *(long *)(param_1 + 8);
    FUN_00811368(*(undefined4 *)(lVar5 + (long)*(int *)(param_1 + 0x10) * 8 + 0xa0));
    FUN_00ab09f4(&local_58);
    *(undefined8 *)(lVar5 + 0xf8) = uStack_50;
    *(undefined8 *)(lVar5 + 0xf0) = local_58;
    *(undefined8 *)(lVar5 + 0x108) = uStack_40;
    *(undefined8 *)(lVar5 + 0x100) = local_48;
    FUN_006a6a54(lVar5,*(undefined4 *)(param_1 + 0x10));
  }
  else {
    if (iVar1 == 3) {
      uVar3 = FUN_0047acf4();
      if (*(long *)(lVar2 + 0x28) == local_38) {
        uVar4 = 0xb;
        goto LAB_006afb28;
      }
      goto LAB_006afba0;
    }
    if (iVar1 == 0) {
      uVar3 = FUN_0047acf4();
      if (*(long *)(lVar2 + 0x28) != local_38) goto LAB_006afba0;
      uVar4 = 10;
LAB_006afb28:
      FUN_0047cdd4(uVar3,uVar4,0);
      return;
    }
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
LAB_006afba0:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
