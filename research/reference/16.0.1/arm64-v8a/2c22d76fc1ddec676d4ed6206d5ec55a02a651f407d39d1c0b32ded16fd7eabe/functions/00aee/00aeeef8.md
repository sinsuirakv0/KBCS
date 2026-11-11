# 00aeeef8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aeeef8",
  "name": "FUN_00aeeef8",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b172516f4df4ea1a4a6c7f40da0bb96b11c154ef365faea44ad12ea3da868fe2",
  "source_text_sha256": "b172516f4df4ea1a4a6c7f40da0bb96b11c154ef365faea44ad12ea3da868fe2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [00658dac](../00658/00658dac.md)
- [00aef0b8](../00aef/00aef0b8.md)
- [00aef0bc](../00aef/00aef0bc.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 1646 bytes

~~~c

void FUN_00aeeef8(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  undefined ***pppuVar4;
  undefined8 uVar5;
  long lVar6;
  undefined **local_60;
  long lStack_58;
  undefined8 local_50;
  long *local_40;
  long local_28;
  
  pppuVar4 = &local_60;
                    /* try { // try from 00aeef00 to 00beef07 has its CatchHandler @ 00aeeff4 */
                    /* try { // try from 00aeef08 to 00bef023 has its CatchHandler @ 00aeee28 */
  lVar2 = tpidr_el0;
  local_28 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lStack_58 = *(long *)(param_1 + 8);
    local_50 = *(undefined8 *)(param_1 + 0x10);
    local_60 = &PTR_FUN_00c8df68;
    local_40 = (long *)&local_60;
    FUN_00658dac(lStack_58 + 0x1fd8,local_50,&local_60);
    if ((undefined ***)local_40 == &local_60) {
      lVar6 = 0x20;
    }
    else {
      if (local_40 == (long *)0x0) goto LAB_00aeefcc;
      lVar6 = 0x28;
      pppuVar4 = (undefined ***)local_40;
    }
    (**(code **)((long)*pppuVar4 + lVar6))();
  }
  else {
    if (iVar1 == 3) {
      uVar3 = FUN_0047acf4();
      if (*(long *)(lVar2 + 0x28) == local_28) {
        uVar5 = 0xb;
        goto LAB_00aeef60;
      }
      goto LAB_00aef038;
    }
    if (iVar1 == 0) {
      uVar3 = FUN_0047acf4();
      if (*(long *)(lVar2 + 0x28) != local_28) goto LAB_00aef038;
      uVar5 = 10;
LAB_00aeef60:
      FUN_0047cdd4(uVar3,uVar5,0);
      return;
    }
  }
LAB_00aeefcc:
  if (*(long *)(lVar2 + 0x28) == local_28) {
    return;
  }
LAB_00aef038:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
