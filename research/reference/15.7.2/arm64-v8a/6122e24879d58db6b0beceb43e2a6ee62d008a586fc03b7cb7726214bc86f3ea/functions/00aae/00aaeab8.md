# 00aaeab8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aaeab8.md)

## 関数情報

~~~json
{
  "address": "00aaeab8",
  "name": "FUN_00aaeab8",
  "size": 612,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "089c14a7cc6388afc70e3aee5bc69e5f489b05c8f6172ebe31dcdb94b7514a8f",
  "source_text_sha256": "089c14a7cc6388afc70e3aee5bc69e5f489b05c8f6172ebe31dcdb94b7514a8f"
}
~~~
## 呼び出し元

- [0076dd00](../0076d/0076dd00.md)

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)
- [0042eb00](../0042e/0042eb00.md)
- [00436518](../00436/00436518.md)
- [005742c4](../00574/005742c4.md)
- [0057462c](../00574/0057462c.md)
- [00aae970](../00aae/00aae970.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb050](../00bdb/00bdb050.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb070](../00bdb/00bdb070.md)
- [00bdb260](../00bdb/00bdb260.md)
- [00bdb290](../00bdb/00bdb290.md)
- [00bdb2a0](../00bdb/00bdb2a0.md)

## 関連文字列（未確認候補）

~~~text
"showPopup"
~~~
## 疑似コード 1/1 / UTF-8 4176 bytes

~~~c

void FUN_00aaeab8(undefined8 *param_1)

{
  byte *pbVar1;
  byte *pbVar2;
  long lVar3;
  undefined *puVar4;
  long *plVar5;
  long *plVar6;
  long lVar7;
  long lVar8;
  byte local_190 [16];
  void *local_180;
  byte local_178;
  char local_177 [8];
  undefined2 local_16f;
  void *local_168;
  long *local_160;
  undefined *local_158 [8];
  ulong local_118;
  undefined8 uStack_110;
  void *local_108;
  undefined8 uStack_100;
  undefined4 local_f8;
  undefined *local_f0 [3];
  undefined8 uStack_d8;
  undefined4 auStack_d0 [4];
  undefined8 local_c0;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  plVar5 = operator_new(0x28);
  pbVar1 = (byte *)*param_1;
  pbVar2 = (byte *)param_1[1];
  *(undefined4 *)(plVar5 + 1) = 6;
  *plVar5 = (long)&PTR_FUN_00bf05b8;
  plVar5[3] = 0;
  plVar5[4] = 0;
  plVar5[2] = 0;
  plVar6 = (long *)PTR_VTT_00c1acc8;
  puVar4 = PTR_vtable_00c1ad98;
  for (; PTR_VTT_00c1acc8 = (undefined *)plVar6, PTR_vtable_00c1ad98 = puVar4, pbVar1 != pbVar2;
      pbVar1 = pbVar1 + 0x18) {
    plVar6 = operator_new(0x28);
    *(undefined4 *)(plVar6 + 1) = 5;
    *plVar6 = (long)&PTR_FUN_00be66a0;
    if ((*pbVar1 & 1) == 0) {
      lVar8 = *(long *)(pbVar1 + 8);
      lVar7 = *(long *)pbVar1;
      plVar6[4] = *(long *)(pbVar1 + 0x10);
      plVar6[3] = lVar8;
      plVar6[2] = lVar7;
    }
    else {
      FUN_00418fe0(plVar6 + 2,*(undefined8 *)(pbVar1 + 0x10),*(undefined8 *)(pbVar1 + 8));
    }
    local_160 = plVar6;
    FUN_0057462c(plVar5,&local_160);
    plVar6 = local_160;
    local_160 = (long *)0x0;
    if (plVar6 != (long *)0x0) {
      (**(code **)(*plVar6 + 8))();
    }
    plVar6 = (long *)PTR_VTT_00c1acc8;
    puVar4 = PTR_vtable_00c1ad98;
  }
  local_c0 = 0;
  local_160 = (long *)plVar6[1];
  local_f0[0] = puVar4 + 0x40;
  *(long *)((long)local_158 + local_160[-3] + -8) = plVar6[2];
  lVar7 = local_160[-3];
  std::__ndk1::ios_base::init((ios_base *)((long)local_158 + lVar7 + -8),local_158);
  local_160 = (long *)(puVar4 + 0x18);
  *(undefined8 *)((long)&uStack_d8 + lVar7) = 0;
  *(undefined4 *)((long)auStack_d0 + lVar7) = 0xffffffff;
  local_f0[0] = puVar4 + 0x40;
  std::__ndk1::basic_streambuf<char,std::__ndk1::char_traits<char>>::basic_streambuf
            ((basic_streambuf<char,std::__ndk1::char_traits<char>> *)local_158);
  puVar4 = PTR_vtable_00c1acd0;
  local_158[0] = PTR_vtable_00c1acd0 + 0x10;
  uStack_110 = 0;
  local_118 = 0;
  uStack_100 = 0;
  local_108 = (void *)0x0;
  local_f8 = 0x10;
  FUN_0042eb00(&local_160,plVar5);
  local_178 = 0x12;
  local_16f = 0x70;
  local_177[0] = s_showPopup_00297307[0];
  local_177[1] = s_showPopup_00297307[1];
  local_177[2] = s_showPopup_00297307[2];
  local_177[3] = s_showPopup_00297307[3];
  local_177[4] = s_showPopup_00297307[4];
  local_177[5] = s_showPopup_00297307[5];
  local_177[6] = s_showPopup_00297307[6];
  local_177[7] = s_showPopup_00297307[7];
  std::__ndk1::basic_stringbuf<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>::
  str();
  FUN_00aae970(&local_178,local_190,1);
  if ((local_190[0] & 1) != 0) {
    operator_delete(local_180);
  }
  if ((local_178 & 1) != 0) {
    operator_delete(local_168);
  }
  local_160 = (long *)*plVar6;
  *(long *)((long)local_158 + local_160[-3] + -8) = plVar6[3];
  local_158[0] = puVar4 + 0x10;
  if ((local_118 & 1) != 0) {
    operator_delete(local_108);
  }
  std::__ndk1::basic_streambuf<char,std::__ndk1::char_traits<char>>::~basic_streambuf
            ((basic_streambuf<char,std::__ndk1::char_traits<char>> *)local_158);
  std::__ndk1::basic_ostream<char,std::__ndk1::char_traits<char>>::~basic_ostream
            ((basic_ostream<char,std::__ndk1::char_traits<char>> *)&local_160);
  std::__ndk1::basic_ios<char,std::__ndk1::char_traits<char>>::~basic_ios
            ((basic_ios<char,std::__ndk1::char_traits<char>> *)local_f0);
  (**(code **)(*plVar5 + 8))(plVar5);
  if (*(long *)(lVar3 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
