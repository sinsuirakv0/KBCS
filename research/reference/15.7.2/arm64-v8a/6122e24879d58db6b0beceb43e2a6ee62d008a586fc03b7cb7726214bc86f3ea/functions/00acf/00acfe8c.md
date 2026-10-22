# 00acfe8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00acfe8c.md)

## 関数情報

~~~json
{
  "address": "00acfe8c",
  "name": "FUN_00acfe8c",
  "size": 448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b9c7c313a71449e635f8a29a193ff67696323d2a2071dc9feb498c2943906a32",
  "source_text_sha256": "b9c7c313a71449e635f8a29a193ff67696323d2a2071dc9feb498c2943906a32"
}
~~~
## 呼び出し元

- [00acfa20](../00acf/00acfa20.md)

## 呼び出し先

- [0053d580](../0053d/0053d580.md)
- [00574730](../00574/00574730.md)
- [00574744](../00574/00574744.md)
- [0057474c](../00574/0057474c.md)
- [00574fec](../00574/00574fec.md)
- [00728090](../00728/00728090.md)
- [00ad05f0](../00ad0/00ad05f0.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 関連文字列（未確認候補）

~~~text
"{\n  \"client\":{\n    \"version\":\"%d\",\n    \"countryCode\":\"%s\"\n  },\n  \"os\":{\n    \"type\":\"%s\",\n    \"version\":\"%s\"\n  },\n  \"device\":{\n    \"model\":\"%s\"\n  }\n}"
~~~
## 疑似コード 1/1 / UTF-8 3950 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00acfe8c(undefined8 param_1)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  long lVar7;
  byte local_d0 [16];
  void *local_c0;
  byte local_b8 [16];
  void *local_a8;
  byte local_a0 [16];
  void *local_90;
  byte local_88 [16];
  void *local_78;
  ulong local_70;
  undefined8 uStack_68;
  char *local_60;
  byte local_50 [16];
  void *local_40;
  undefined1 auStack_38 [8];
  __shared_weak_count *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  local_60 = operator_new(0x98);
  uStack_68 = _UNK_002b1198;
  local_70 = _DAT_002b1190;
  local_60[0x94] = '\0';
  local_60[0x90] = ' ';
  uVar6 = s____client_____version____d____co_0029a50b._136_8_;
  uVar5 = s____client_____version____d____co_0029a50b._128_8_;
  uVar4 = s____client_____version____d____co_0029a50b._120_8_;
  uVar3 = s____client_____version____d____co_0029a50b._112_8_;
  uVar2 = s____client_____version____d____co_0029a50b._96_8_;
  local_60[0x91] = '}';
  local_60[0x92] = '\n';
  local_60[0x93] = '}';
  *(undefined8 *)(local_60 + 0x68) = s____client_____version____d____co_0029a50b._104_8_;
  *(undefined8 *)(local_60 + 0x60) = uVar2;
  *(undefined8 *)(local_60 + 0x78) = uVar4;
  *(undefined8 *)(local_60 + 0x70) = uVar3;
  *(undefined8 *)(local_60 + 0x88) = uVar6;
  *(undefined8 *)(local_60 + 0x80) = uVar5;
  uVar4 = s____client_____version____d____co_0029a50b._56_8_;
  uVar3 = s____client_____version____d____co_0029a50b._48_8_;
  uVar2 = s____client_____version____d____co_0029a50b._32_8_;
  *(undefined8 *)(local_60 + 0x28) = s____client_____version____d____co_0029a50b._40_8_;
  *(undefined8 *)(local_60 + 0x20) = uVar2;
  *(undefined8 *)(local_60 + 0x38) = uVar4;
  *(undefined8 *)(local_60 + 0x30) = uVar3;
  uVar4 = s____client_____version____d____co_0029a50b._88_8_;
  uVar3 = s____client_____version____d____co_0029a50b._80_8_;
  uVar2 = s____client_____version____d____co_0029a50b._64_8_;
  *(undefined8 *)(local_60 + 0x48) = s____client_____version____d____co_0029a50b._72_8_;
  *(undefined8 *)(local_60 + 0x40) = uVar2;
  *(undefined8 *)(local_60 + 0x58) = uVar4;
  *(undefined8 *)(local_60 + 0x50) = uVar3;
  uVar4 = s____client_____version____d____co_0029a50b._24_8_;
  uVar3 = s____client_____version____d____co_0029a50b._16_8_;
  uVar2 = s____client_____version____d____co_0029a50b._0_8_;
  *(undefined8 *)(local_60 + 8) = s____client_____version____d____co_0029a50b._8_8_;
  *(undefined8 *)local_60 = uVar2;
  *(undefined8 *)(local_60 + 0x18) = uVar4;
  *(undefined8 *)(local_60 + 0x10) = uVar3;
  FUN_00728090(local_88);
  thunk_FUN_00568a44(local_a0);
  thunk_FUN_0056bfc8(local_b8);
  thunk_FUN_00568c04(local_d0);
  FUN_00ad05f0(local_50,&local_70,0x24cae,local_88,local_a0,local_b8,local_d0);
  thunk_FUN_00567ef0(auStack_38,local_50);
  thunk_FUN_0055dbb0(param_1,auStack_38,0);
  if ((local_30 != (__shared_weak_count *)0x0) &&
     (lVar7 = FUN_00bd6d90(0xffffffffffffffff,local_30 + 8), lVar7 == 0)) {
    (**(code **)(*(long *)local_30 + 0x10))(local_30);
    std::__ndk1::__shared_weak_count::__release_weak(local_30);
  }
  if ((local_50[0] & 1) != 0) {
    operator_delete(local_40);
  }
  if ((local_d0[0] & 1) != 0) {
    operator_delete(local_c0);
  }
  if ((local_b8[0] & 1) != 0) {
    operator_delete(local_a8);
  }
  if ((local_a0[0] & 1) != 0) {
    operator_delete(local_90);
  }
  if ((local_88[0] & 1) != 0) {
    operator_delete(local_78);
  }
  if ((local_70 & 1) != 0) {
    operator_delete(local_60);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
