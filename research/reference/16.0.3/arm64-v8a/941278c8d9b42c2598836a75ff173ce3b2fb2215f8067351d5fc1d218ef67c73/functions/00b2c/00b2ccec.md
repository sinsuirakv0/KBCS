# 00b2ccec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00b2ccec",
  "name": "FUN_00b2ccec",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d112cd3313d6d2f26e47d5d44b437f5995ff491f19586fb54987336dba220ad9",
  "source_text_sha256": "d112cd3313d6d2f26e47d5d44b437f5995ff491f19586fb54987336dba220ad9"
}
~~~

## 呼び出し元

- [00b2ded8](../00b2d/00b2ded8.md)

## 呼び出し先

- [00576618](../00576/00576618.md)
- [005891cc](../00589/005891cc.md)
- [005894a4](../00589/005894a4.md)
- [005894bc](../00589/005894bc.md)
- [00589680](../00589/00589680.md)
- [00589bb0](../00589/00589bb0.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

## 関連文字列（未確認候補）

~~~text
"getSafeInsetTop"
~~~

## 疑似コード / UTF-8 2090 bytes

~~~c

void FUN_00b2ccec(void)

{
  long lVar1;
  char cVar2;
  undefined4 uVar3;
  long *plVar4;
  undefined8 uVar5;
  ulong uVar6;
  byte local_70 [16];
  void *local_60;
  byte local_58;
  char local_57 [7];
  char cStack_50;
  char acStack_4f [7];
  undefined1 local_48;
  undefined7 uStack_47;
  long local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  plVar4 = (long *)FUN_005891cc();
  uVar5 = FUN_005894bc();
  local_58 = 0x1e;
  local_48 = 0;
  local_57[0] = s_getSafeInsetTop_002a6096[0];
  local_57[1] = s_getSafeInsetTop_002a6096[1];
  local_57[2] = s_getSafeInsetTop_002a6096[2];
  local_57[3] = s_getSafeInsetTop_002a6096[3];
  local_57[4] = s_getSafeInsetTop_002a6096[4];
  local_57[5] = s_getSafeInsetTop_002a6096[5];
  local_57[6] = s_getSafeInsetTop_002a6096[6];
  cStack_50 = s_getSafeInsetTop_002a6096[7];
  acStack_4f[0] = s_getSafeInsetTop_002a6096[8];
  acStack_4f[1] = s_getSafeInsetTop_002a6096[9];
  acStack_4f[2] = s_getSafeInsetTop_002a6096[10];
  acStack_4f[3] = s_getSafeInsetTop_002a6096[0xb];
  acStack_4f[4] = s_getSafeInsetTop_002a6096[0xc];
  acStack_4f[5] = s_getSafeInsetTop_002a6096[0xd];
  acStack_4f[6] = s_getSafeInsetTop_002a6096[0xe];
  local_70[0] = 6;
  local_70[1] = 0x28;
  local_70[2] = 0x29;
  local_70[3] = 0x49;
  local_70[4] = 0;
  local_40 = FUN_00589680(uVar5,&local_58,local_70,plVar4);
  if ((local_70[0] & 1) != 0) {
    _ZdlPv(local_60);
  }
  if ((local_58 & 1) != 0) {
    _ZdlPv((void *)CONCAT71(uStack_47,local_48));
  }
  uVar6 = FUN_005894a4(&local_40);
  if ((uVar6 & 1) != 0) {
    FUN_005894bc();
    uVar5 = FUN_00589bb0();
    if (local_40 != 0) {
      uVar3 = FUN_00576618(plVar4,uVar5);
      cVar2 = (**(code **)(*plVar4 + 0x720))(plVar4);
      if (cVar2 != '\0') {
        (**(code **)(*plVar4 + 0x80))(plVar4);
        (**(code **)(*plVar4 + 0x88))(plVar4);
      }
      goto LAB_00b2cdf4;
    }
  }
  uVar3 = 0;
LAB_00b2cdf4:
  if (*(long *)(lVar1 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(uVar3);
  }
  return;
}

~~~
