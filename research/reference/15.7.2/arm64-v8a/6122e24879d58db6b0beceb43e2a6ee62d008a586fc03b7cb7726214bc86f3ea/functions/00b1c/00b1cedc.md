# 00b1cedc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b1cedc.md)

## 関数情報

~~~json
{
  "address": "00b1cedc",
  "name": "flatbuffers::Parser::ParseNestedFlatbuffer",
  "size": 1312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "54a8fc1c7f227c0af8731d1a32b84121761da1f66d32251300b1616ee77268d5",
  "source_text_sha256": "54a8fc1c7f227c0af8731d1a32b84121761da1f66d32251300b1616ee77268d5"
}
~~~
## 呼び出し元

- [00bdf850](../00bdf/00bdf850.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bde1c0](../00bde/00bde1c0.md)
- [00bde910](../00bde/00bde910.md)
- [00bde970](../00bde/00bde970.md)
- [00bde980](../00bde/00bde980.md)
- [00bdeab0](../00bde/00bdeab0.md)
- [00bdef60](../00bde/00bdef60.md)
- [00bdf060](../00bdf/00bdf060.md)
- [00bdf0b0](../00bdf/00bdf0b0.md)
- [00bdf290](../00bdf/00bdf290.md)
- [00bdf380](../00bdf/00bdf380.md)
- [00bdf3c0](../00bdf/00bdf3c0.md)
- [00bdf700](../00bdf/00bdf700.md)
- [00bdf800](../00bdf/00bdf800.md)
- [00bdf8d0](../00bdf/00bdf8d0.md)
- [00bdfe60](../00bdf/00bdfe60.md)
- [00bdffc0](../00bdf/00bdffc0.md)

## 関連文字列（未確認候補）

~~~text
"_generated"
"error: "
"std::unique_ptr"
~~~
## 疑似コード 1/1 / UTF-8 14791 bytes

~~~c

/* flatbuffers::Parser::ParseNestedFlatbuffer(flatbuffers::Value&, flatbuffers::FieldDef*, unsigned
   long, flatbuffers::StructDef const*) */

void flatbuffers::Parser::ParseNestedFlatbuffer
               (Value *param_1,FieldDef *param_2,ulong param_3,StructDef *param_4)

{
  vector_downward *this;
  long lVar1;
  undefined8 *puVar2;
  bool bVar3;
  undefined8 uVar4;
  uint uVar5;
  char **ppcVar6;
  char **ppcVar7;
  basic_string *pbVar8;
  uint in_w4;
  char *in_x8;
  undefined1 *puVar9;
  ulong uVar10;
  ulong uVar11;
  undefined8 *puVar12;
  ulong uVar13;
  FieldDef *pFVar14;
  char **ppcVar15;
  char **ppcVar16;
  char **ppcVar17;
  long lVar18;
  long lVar19;
  char *pcVar20;
  char *pcVar21;
  char *pcVar22;
  ulong local_6d8;
  ulong local_6d0;
  char **local_6c8;
  uint local_6c0;
  undefined2 uStack_6bc;
  undefined2 uStack_6ba;
  undefined8 uStack_6b8;
  void *local_6b0;
  undefined1 local_6a8;
  undefined1 local_6a0;
  char acStack_69f [7];
  char local_698;
  char acStack_697 [7];
  undefined8 local_690;
  undefined8 uStack_688;
  undefined8 local_680;
  undefined8 uStack_678;
  undefined4 local_670;
  undefined8 local_668;
  undefined8 uStack_660;
  undefined8 local_658;
  undefined8 uStack_650;
  undefined8 local_648;
  undefined8 uStack_640;
  undefined2 local_638;
  undefined1 local_636;
  undefined8 local_630;
  undefined8 uStack_628;
  undefined5 uStack_620;
  undefined3 local_61b;
  undefined5 uStack_618;
  undefined8 local_610;
  undefined8 uStack_608;
  undefined8 local_600;
  undefined8 uStack_5f8;
  undefined8 uStack_5f0;
  undefined8 uStack_5e8;
  undefined4 local_5e0;
  undefined8 local_5d8;
  undefined8 uStack_5d0;
  undefined7 local_5c8;
  undefined4 uStack_5c1;
  undefined8 local_5b8;
  undefined8 uStack_5b0;
  undefined8 uStack_5a8;
  undefined8 uStack_5a0;
  undefined8 local_598;
  undefined8 uStack_590;
  undefined8 uStack_588;
  undefined8 uStack_580;
  undefined8 local_578;
  undefined1 uStack_570;
  undefined7 uStack_56f;
  char cStack_568;
  undefined2 local_567;
  undefined1 local_565;
  undefined4 uStack_564;
  undefined8 uStack_560;
  undefined8 local_558;
  undefined8 local_550;
  undefined8 uStack_548;
  undefined8 local_540;
  undefined8 local_538;
  undefined2 local_530;
  Parser aPStack_528 [176];
  __tree_node **local_478;
  __tree_node *local_470;
  undefined8 local_468;
  undefined8 local_460;
  undefined8 local_458;
  char acStack_3f0 [56];
  uint local_3b8;
  uint local_3b0;
  int local_3a8;
  undefined4 uStack_3a4;
  ulong local_390;
  undefined8 local_2e8;
  IDLOptions aIStack_250 [408];
  Value local_b8;
  long local_70;
  
  lVar1 = tpidr_el0;
  local_70 = *(long *)(lVar1 + 0x28);
  if (*(int *)(param_1 + 0x14) == 0x5b) {
    ParseAnyValue(param_1,param_2,param_3,param_4,in_w4,false);
    in_x8[1] = '\x01';
    if (*in_x8 != '\0') goto LAB_00b1d3c4;
  }
  else {
    lVar18 = *(long *)param_1;
    SkipAnyJsonValue();
    in_x8[1] = '\x01';
    if (*in_x8 != '\0') goto LAB_00b1d3c4;
    lVar19 = *(long *)param_1;
    ppcVar15 = (char **)(lVar18 + -1);
    local_6d0 = 0;
    local_6c8 = (char **)0x0;
    local_6d8 = 0;
    ppcVar17 = (char **)(lVar19 + -1);
    uVar13 = (long)ppcVar17 - (long)ppcVar15;
    if (0xffffffffffffffef < uVar13) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    if (uVar13 < 0x17) {
      local_6d8 = (ulong)(byte)((int)uVar13 << 1);
      ppcVar6 = (char **)((ulong)&local_6d8 | 1);
    }
    else {
      uVar10 = uVar13 + 0x10 & 0xfffffffffffffff0;
      ppcVar6 = operator_new(uVar10);
      local_6d8 = uVar10 | 1;
      local_6d0 = uVar13;
      local_6c8 = ppcVar6;
    }
    if (lVar18 != lVar19) {
      uVar13 = lVar19 - lVar18;
      ppcVar7 = ppcVar6;
      if ((0x1f < uVar13) &&
         ((ppcVar17 <= ppcVar6 || ((char **)((long)ppcVar6 + uVar13) <= ppcVar15)))) {
        uVar11 = uVar13 & 0xffffffffffffffe0;
        ppcVar7 = ppcVar6 + 2;
        ppcVar6 = (char **)((long)ppcVar6 + uVar11);
        puVar12 = (undefined8 *)(lVar18 + 0xf);
        uVar10 = uVar11;
        do {
          puVar2 = puVar12 + -1;
          pcVar20 = (char *)puVar12[-2];
          pcVar22 = (char *)puVar12[1];
          pcVar21 = (char *)*puVar12;
          uVar10 = uVar10 - 0x20;
          puVar12 = puVar12 + 4;
          ppcVar7[-1] = (char *)*puVar2;
          ppcVar7[-2] = pcVar20;
          ppcVar7[1] = pcVar22;
          *ppcVar7 = pcVar21;
          ppcVar7 = ppcVar7 + 4;
        } while (uVar10 != 0);
        ppcVar7 = ppcVar6;
        ppcVar15 = (char **)((long)ppcVar15 + uVar11);
        if (uVar13 == uVar11) goto LAB_00b1d044;
      }
      do {
        ppcVar16 = (char **)((long)ppcVar15 + 1);
        ppcVar6 = (char **)((long)ppcVar7 + 1);
        *(undefined1 *)ppcVar7 = *(undefined1 *)ppcVar15;
        ppcVar7 = ppcVar6;
        ppcVar15 = ppcVar16;
      } while (ppcVar17 != ppcVar16);
    }
LAB_00b1d044:
    local_540 = DAT_002b2820;
    uVar4 = s__generated_002ac2f1._0_8_;
    uStack_6b8 = 0x100010100000002;
    local_6b0 = (void *)0x0;
    local_6a0 = 0x1e;
    uStack_6bc = 0;
    acStack_69f[0] = s_std__unique_ptr_00298725[0];
    acStack_69f[1] = s_std__unique_ptr_00298725[1];
    acStack_69f[2] = s_std__unique_ptr_00298725[2];
    acStack_69f[3] = s_std__unique_ptr_00298725[3];
    acStack_69f[4] = s_std__unique_ptr_00298725[4];
    acStack_69f[5] = s_std__unique_ptr_00298725[5];
    acStack_69f[6] = s_std__unique_ptr_00298725[6];
    local_6c0 = 0;
    local_6a8 = 0;
    uStack_688 = 0;
    local_690 = 0;
    local_670 = 0;
    local_680 = 0;
    uStack_678 = 0;
    local_698 = s_std__unique_ptr_00298725[7];
    acStack_697[0] = s_std__unique_ptr_00298725[8];
    acStack_697[1] = s_std__unique_ptr_00298725[9];
    acStack_697[2] = s_std__unique_ptr_00298725[10];
    acStack_697[3] = s_std__unique_ptr_00298725[0xb];
    acStack_697[4] = s_std__unique_ptr_00298725[0xc];
    acStack_697[5] = s_std__unique_ptr_00298725[0xd];
    acStack_697[6] = s_std__unique_ptr_00298725[0xe];
    uStack_640 = 0;
    local_648 = 0;
    local_658 = 0;
    uStack_660 = 0;
    local_668 = 0;
    uStack_650 = 0x5402;
    local_638 = 1;
    local_636 = 0;
    local_630 = 0;
    uStack_628 = 0;
    uStack_618 = 0;
    uStack_620 = 0;
    local_61b = 0;
    uStack_5f8 = 0;
    local_600 = 0;
    uStack_5e8 = 0;
    uStack_5f0 = 0;
    uStack_608 = 0;
    local_610 = 0;
    local_5e0 = 1;
    local_5d8 = 0;
    uStack_5d0 = 0;
    local_5c8 = 0;
    uStack_5c1 = 0;
    local_578 = 0;
    uStack_560 = 0;
    uStack_564 = 0;
    uStack_590 = 0;
    local_598 = 0;
    uStack_580 = 0;
    uStack_588 = 0;
    uStack_5b0 = 0;
    local_5b8 = 0;
    uStack_5a0 = 0;
    uStack_5a8 = 0;
    uStack_570 = 0x14;
    local_567 = 0x6465;
    *(undefined1 *)ppcVar6 = 0;
    uStack_56f = (undefined7)uVar4;
    cStack_568 = SUB81(uVar4,7);
    local_565 = 0;
    local_550 = 0;
    uStack_548 = 0;
    local_558 = 0;
    local_538 = 0;
    local_530 = 0x101;
    Parser(aPStack_528,(IDLOptions *)&local_6c0);
    IDLOptions::~IDLOptions((IDLOptions *)&local_6c0);
    local_2e8 = *(undefined8 *)(param_3 + 0xe0);
    if (aPStack_528 != (Parser *)param_1) {
      std::__ndk1::
      __tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>>>
      ::
      __assign_multi<std::__ndk1::__tree_const_iterator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::__tree_node<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,void*>*,long>>
                ((__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>>>
                  *)&local_478,*(undefined8 *)(param_1 + 0xb0),param_1 + 0xb8);
      std::__ndk1::vector<flatbuffers::EnumDef*,std::__ndk1::allocator<flatbuffers::EnumDef*>>::
      assign<flatbuffers::EnumDef**>
                ((vector<flatbuffers::EnumDef*,std::__ndk1::allocator<flatbuffers::EnumDef*>> *)
                 &local_460,*(EnumDef ***)(param_1 + 200),*(EnumDef ***)(param_1 + 0xd0));
    }
    IDLOptions::operator=(aIStack_250,(IDLOptions *)(param_1 + 0x2d8));
    local_b8 = param_1[0x470];
    ppcVar15 = (char **)((ulong)&local_6d8 | 1);
    if ((local_6d8 & 1) != 0) {
      ppcVar15 = local_6c8;
    }
    pbVar8 = (basic_string *)0x0;
    uVar13 = Parse((char *)aPStack_528,ppcVar15,(char *)0x0);
    std::__ndk1::
    __tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>>>
    ::destroy((__tree<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::__map_value_compare<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>,std::__ndk1::less<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>>,true>,std::__ndk1::allocator<std::__ndk1::__value_type<std::__ndk1::basic_string<char,std::__ndk1::char_traits<char>,std::__ndk1::allocator<char>>,flatbuffers::EnumDef*>>>
               *)&local_478,local_470);
    local_470 = (__tree_node *)0x0;
    local_468 = 0;
    local_458 = local_460;
    local_478 = &local_470;
    if ((uVar13 & 1) == 0) {
      std::__ndk1::operator+((__ndk1 *)"error: ",acStack_3f0,pbVar8);
      Message((Parser *)param_1,(basic_string *)&local_6c0);
      if ((local_6c0 & 1) != 0) {
        operator_delete(local_6b0);
      }
      in_x8[0] = '\x01';
      in_x8[1] = '\x01';
      bVar3 = true;
    }
    else {
      this = (vector_downward *)(param_1 + 0x150);
      if (*(ulong *)(param_1 + 0x198) < local_390) {
        *(ulong *)(param_1 + 0x198) = local_390;
      }
      lVar18 = *(long *)(param_1 + 0x180);
      uVar13 = local_390 - 1 &
               -((ulong)((local_3b8 - local_3a8) + local_3b0) +
                (ulong)(uint)((*(int *)(param_1 + 0x170) - (int)lVar18) + *(int *)(param_1 + 0x178))
                );
      if ((ulong)(lVar18 - *(long *)(param_1 + 0x188)) < uVar13) {
        vector_downward::reallocate(this,uVar13);
        puVar9 = (undefined1 *)(*(long *)(param_1 + 0x180) - uVar13);
        *(undefined1 **)(param_1 + 0x180) = puVar9;
LAB_00b1d2bc:
        *puVar9 = 0;
        if (uVar13 != 1) {
          uVar10 = 1;
          do {
            *(undefined1 *)(*(long *)(param_1 + 0x180) + uVar10) = 0;
            uVar10 = uVar10 + 1;
          } while (uVar13 != uVar10);
        }
      }
      else {
        puVar9 = (undefined1 *)(lVar18 - uVar13);
        *(undefined1 **)(param_1 + 0x180) = puVar9;
        if (uVar13 != 0) goto LAB_00b1d2bc;
      }
      uVar13 = ((ulong)local_3b8 - (long)CONCAT44(uStack_3a4,local_3a8)) + (ulong)local_3b0;
      uVar10 = uVar13 & 0xffffffff;
      FlatBufferBuilder::StartVector((FlatBufferBuilder *)this,uVar10,1);
      if (uVar10 != 0) {
        lVar18 = *(long *)(param_1 + 0x180);
        if ((ulong)(lVar18 - *(long *)(param_1 + 0x188)) < uVar10) {
          vector_downward::reallocate(this,uVar10);
          lVar18 = *(long *)(param_1 + 0x180);
        }
        *(void **)(param_1 + 0x180) = (void *)(lVar18 - uVar10);
        memcpy((void *)(lVar18 - uVar10),(void *)CONCAT44(uStack_3a4,local_3a8),uVar10);
      }
      param_1[0x196] = (Value)0x0;
      uVar5 = FlatBufferBuilder::PushElement<unsigned_int>((FlatBufferBuilder *)this,(uint)uVar13);
      NumToString<unsigned_int>(uVar5);
      pFVar14 = param_2 + 0x20;
      if (((byte)*pFVar14 & 1) == 0) {
        *(undefined2 *)pFVar14 = 0;
      }
      else {
        **(undefined1 **)(param_2 + 0x30) = 0;
        *(undefined8 *)(param_2 + 0x28) = 0;
        if (((byte)param_2[0x20] & 1) != 0) {
          operator_delete(*(void **)(param_2 + 0x30));
          *(undefined8 *)(param_2 + 0x20) = 0;
        }
      }
      bVar3 = false;
      *(void **)(param_2 + 0x30) = local_6b0;
      *(undefined8 *)(param_2 + 0x28) = uStack_6b8;
      *(ulong *)pFVar14 = CONCAT26(uStack_6ba,CONCAT24(uStack_6bc,local_6c0));
    }
    ~Parser(aPStack_528);
    if ((local_6d8 & 1) != 0) {
      operator_delete(local_6c8);
    }
    if (bVar3) goto LAB_00b1d3c4;
  }
  in_x8[0] = '\0';
  in_x8[1] = '\0';
LAB_00b1d3c4:
  if (*(long *)(lVar1 + 0x28) != local_70) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~
