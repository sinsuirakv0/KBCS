# 00acbecc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00acbecc",
  "name": "FUN_00acbecc",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "61b4a42f893a3676389a35a3dd690f1d9711445d06fe4620a2d8d7d554ce2474",
  "source_text_sha256": "61b4a42f893a3676389a35a3dd690f1d9711445d06fe4620a2d8d7d554ce2474"
}
~~~

## 呼び出し元

- [00accf4c](../00acc/00accf4c.md)

## 呼び出し先

- [005533e0](../00553/005533e0.md)
- [00565f94](../00565/00565f94.md)
- [0056626c](../00566/0056626c.md)
- [00566284](../00566/00566284.md)
- [00566448](../00566/00566448.md)
- [00566978](../00566/00566978.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

## 関連文字列（未確認候補）

~~~text
"getSafeInsetBottom"
~~~

## 疑似コード / UTF-8 1977 bytes

~~~c

void FUN_00acbecc(void)

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
  char local_57 [8];
  undefined7 uStack_4f;
  char cStack_48;
  undefined2 uStack_47;
  undefined1 uStack_45;
  undefined4 uStack_44;
  long local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  plVar4 = (long *)FUN_00565f94();
  uVar5 = FUN_00566284();
  local_58 = 0x24;
  local_70[0] = 6;
  uStack_47 = 0x6d6f;
  uStack_4f = (undefined7)s_getSafeInsetBottom_0029bcec._8_8_;
  cStack_48 = SUB81(s_getSafeInsetBottom_0029bcec._8_8_,7);
  local_57[0] = s_getSafeInsetBottom_0029bcec[0];
  local_57[1] = s_getSafeInsetBottom_0029bcec[1];
  local_57[2] = s_getSafeInsetBottom_0029bcec[2];
  local_57[3] = s_getSafeInsetBottom_0029bcec[3];
  local_57[4] = s_getSafeInsetBottom_0029bcec[4];
  local_57[5] = s_getSafeInsetBottom_0029bcec[5];
  local_57[6] = s_getSafeInsetBottom_0029bcec[6];
  local_57[7] = s_getSafeInsetBottom_0029bcec[7];
  uStack_45 = 0;
  local_70[1] = 0x28;
  local_70[2] = 0x29;
  local_70[3] = 0x49;
  local_70[4] = 0;
  local_40 = FUN_00566448(uVar5,&local_58,local_70,plVar4);
  if ((local_70[0] & 1) != 0) {
    _ZdlPv(local_60);
  }
  if ((local_58 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_44,CONCAT13(uStack_45,CONCAT21(uStack_47,cStack_48))));
  }
  uVar6 = FUN_0056626c(&local_40);
  if ((uVar6 & 1) != 0) {
    FUN_00566284();
    uVar5 = FUN_00566978();
    if (local_40 != 0) {
      uVar3 = FUN_005533e0(plVar4,uVar5);
      cVar2 = (**(code **)(*plVar4 + 0x720))(plVar4);
      if (cVar2 != '\0') {
        (**(code **)(*plVar4 + 0x80))(plVar4);
        (**(code **)(*plVar4 + 0x88))(plVar4);
      }
      goto LAB_00acbfd4;
    }
  }
  uVar3 = 0;
LAB_00acbfd4:
  if (*(long *)(lVar1 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(uVar3);
  }
  return;
}

~~~
