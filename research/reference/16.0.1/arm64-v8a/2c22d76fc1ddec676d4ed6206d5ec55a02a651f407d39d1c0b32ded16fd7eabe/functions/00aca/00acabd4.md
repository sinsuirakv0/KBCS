# 00acabd4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00acabd4",
  "name": "FUN_00acabd4",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95e567a8a76353566504c71df91884abca034a093dd979ee08837847757e3aa9",
  "source_text_sha256": "95e567a8a76353566504c71df91884abca034a093dd979ee08837847757e3aa9"
}
~~~

## 呼び出し元

- [0078bd58](../0078b/0078bd58.md)
- [0078bfc4](../0078b/0078bfc4.md)
- [0078df38](../0078d/0078df38.md)
- [0078e6a4](../0078e/0078e6a4.md)
- [0078e91c](../0078e/0078e91c.md)
- [0078eb30](../0078e/0078eb30.md)
- [00838ba0](../00838/00838ba0.md)
- [008cf91c](../008cf/008cf91c.md)
- [008d0710](../008d0/008d0710.md)
- [008d8404](../008d8/008d8404.md)
- [008d9534](../008d9/008d9534.md)
- [008fd500](../008fd/008fd500.md)
- [009015dc](../00901/009015dc.md)
- [009d0320](../009d0/009d0320.md)
- [00a3ce18](../00a3c/00a3ce18.md)
- [00a40d90](../00a40/00a40d90.md)
- [00a73530](../00a73/00a73530.md)
- [00ac3350](../00ac3/00ac3350.md)

## 呼び出し先

- [0057bea8](../0057b/0057bea8.md)
- [008514f8](../00851/008514f8.md)
- [00ac9594](../00ac9/00ac9594.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 1052 bytes

~~~c

void FUN_00acabd4(long param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  long *plVar3;
  long *plVar4;
  long local_70 [4];
  long *local_50;
  long local_38;
  
  plVar4 = local_70;
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  lVar2 = FUN_008514f8();
  plVar3 = (long *)param_2[4];
  *(undefined1 *)((long)&fde_table_entry_00332a20.data_loc + lVar2 + 1) = 1;
  if (plVar3 == (long *)0x0) {
    local_50 = (long *)0x0;
  }
  else if (plVar3 == param_2) {
    local_50 = local_70;
    (**(code **)(*param_2 + 0x18))(param_2,local_70);
  }
  else {
    local_50 = (long *)(**(code **)(*plVar3 + 0x10))();
  }
  FUN_0057bea8(local_70,param_1 + 0xe0);
  if (local_50 == local_70) {
    lVar2 = 0x20;
  }
  else {
    if (local_50 == (long *)0x0) goto LAB_00acac98;
    lVar2 = 0x28;
    plVar4 = local_50;
  }
  (**(code **)(*plVar4 + lVar2))();
LAB_00acac98:
  FUN_00ac9594(param_1);
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
