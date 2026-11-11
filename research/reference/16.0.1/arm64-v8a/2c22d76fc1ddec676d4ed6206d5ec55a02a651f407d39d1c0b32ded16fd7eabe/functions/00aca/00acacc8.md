# 00acacc8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00acacc8",
  "name": "FUN_00acacc8",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ee35d251443d76ee4cdfb00a0a9e061025745981e4d8b8c08e07a320dfb8c1ef",
  "source_text_sha256": "ee35d251443d76ee4cdfb00a0a9e061025745981e4d8b8c08e07a320dfb8c1ef"
}
~~~

## 呼び出し元

- [006af39c](../006af/006af39c.md)
- [00830e9c](../00830/00830e9c.md)

## 呼び出し先

- [0057bea8](../0057b/0057bea8.md)
- [00ac9594](../00ac9/00ac9594.md)
- [00c57ee0](../00c57/00c57ee0.md)

## 疑似コード / UTF-8 1026 bytes

~~~c

void FUN_00acacc8(long param_1,long *param_2)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  long local_70 [4];
  long *local_50;
  long local_38;
  
  local_50 = local_70;
  plVar3 = local_70;
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  plVar2 = (long *)param_2[4];
  *(undefined1 *)(param_1 + 0xa0) = 1;
  *(undefined4 *)(param_1 + 0xa4) = 0;
  if (plVar2 == (long *)0x0) {
    local_50 = (long *)0x0;
  }
  else if (plVar2 == param_2) {
    (**(code **)(*param_2 + 0x18))(param_2,local_70);
  }
  else {
    local_50 = (long *)(**(code **)(*plVar2 + 0x10))();
  }
  FUN_0057bea8(local_70,param_1 + 0x140);
  if (local_50 == local_70) {
    lVar4 = 0x20;
  }
  else {
    if (local_50 == (long *)0x0) goto LAB_00acad7c;
    lVar4 = 0x28;
    plVar3 = local_50;
  }
  (**(code **)(*plVar3 + lVar4))();
LAB_00acad7c:
  FUN_00ac9594(param_1);
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
