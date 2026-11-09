# 00aeead0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aeead0",
  "name": "FUN_00aeead0",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3c490b71a15511ef97d2d2b4a6e870d85fb02aca96afa0aa1c210309822a972a",
  "source_text_sha256": "3c490b71a15511ef97d2d2b4a6e870d85fb02aca96afa0aa1c210309822a972a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [00658d6c](../00658/00658d6c.md)
- [00aeec90](../00aee/00aeec90.md)
- [00aeec94](../00aee/00aeec94.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 疑似コード / UTF-8 1623 bytes

~~~c

void FUN_00aeead0(long param_1,undefined8 param_2,int *param_3)

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
                    /* catch() { ... } // from try @ 00aee878 with catch @ 00aeead4
                       catch() { ... } // from try @ 00aeeab8 with catch @ 00aeead4 */
  lVar2 = tpidr_el0;
  local_28 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lStack_58 = *(long *)(param_1 + 8);
    local_50 = *(undefined8 *)(param_1 + 0x10);
    local_60 = &PTR_FUN_00c8db68;
    local_40 = (long *)&local_60;
    FUN_00658d6c(lStack_58 + 0x1fd8,local_50,&local_60);
    if ((undefined ***)local_40 == &local_60) {
      lVar6 = 0x20;
    }
    else {
      if (local_40 == (long *)0x0) goto LAB_00aeeba4;
      lVar6 = 0x28;
      pppuVar4 = (undefined ***)local_40;
    }
    (**(code **)((long)*pppuVar4 + lVar6))();
  }
  else {
    if (iVar1 == 3) {
      uVar3 = FUN_0047acb4();
      if (*(long *)(lVar2 + 0x28) == local_28) {
        uVar5 = 0xb;
        goto LAB_00aeeb38;
      }
      goto LAB_00aeec10;
    }
    if (iVar1 == 0) {
      uVar3 = FUN_0047acb4();
      if (*(long *)(lVar2 + 0x28) != local_28) goto LAB_00aeec10;
      uVar5 = 10;
LAB_00aeeb38:
      FUN_0047cd94(uVar3,uVar5,0);
      return;
    }
  }
LAB_00aeeba4:
  if (*(long *)(lVar2 + 0x28) == local_28) {
    return;
  }
LAB_00aeec10:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
