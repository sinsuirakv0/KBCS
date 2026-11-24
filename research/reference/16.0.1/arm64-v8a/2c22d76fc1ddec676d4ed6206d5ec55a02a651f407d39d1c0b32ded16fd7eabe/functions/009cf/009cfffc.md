# 009cfffc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0079.md#review-847e86c635a9041befb13ab3b1ff2a01)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0038.md#review-847e86c635a9041befb13ab3b1ff2a01)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009cfffc",
  "name": "FUN_009cfffc",
  "size": 724,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3835e6ae4a0a51e1ff7801217d9de4ec9f697bdc8ea3e6510104dd3cfee72e98",
  "source_text_sha256": "3835e6ae4a0a51e1ff7801217d9de4ec9f697bdc8ea3e6510104dd3cfee72e98",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009cfffc",
        "009d02cb"
      ],
      [
        "009d031c",
        "009d031f"
      ]
    ],
    "bytes_sha256": "c1dbcfa9b4097a6fa36f3be813b25d411f11648dc4d6c168fd4c16238e977fa8",
    "instruction_count": 181,
    "instruction_bytes": 724,
    "body_bytes": 724,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b1f428](../00b1f/00b1f428.md)

## 呼び出し先

- [0048791c](../00487/0048791c.md)
- [0048793c](../00487/0048793c.md)
- [00487e20](../00487/00487e20.md)
- [00488558](../00488/00488558.md)
- [00488658](../00488/00488658.md)
- [00b110ec](../00b11/00b110ec.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57fa0](../00c57/00c57fa0.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c58090](../00c58/00c58090.md)

## 関連文字列（未確認候補）

~~~text
"rankGift.csv"
"unitlimit.csv"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 13111 bytes

~~~c

void FUN_009cfffc(long param_1)

{
  long lVar1;
  byte *pbVar2;
  undefined *puVar3;
  undefined *puVar4;
  bool bVar5;
  int iVar6;
  ulong uVar7;
  void *__s;
  byte *pbVar8;
  long lVar9;
  byte local_1b8;
  undefined5 local_1b7;
  undefined3 uStack_1b2;
  undefined4 local_1af;
  char local_1ab;
  undefined1 local_1aa;
  void *local_1a8;
  undefined **local_1a0;
  void *local_198;
  void *local_190;
  byte local_180;
  void *local_170;
  long local_158;
  undefined *local_150 [8];
  byte local_110;
  void *local_100;
  undefined1 auStack_e8 [160];
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  FUN_00487e20(&local_1a0);
  local_1a0 = &PTR_FUN_00c64d38;
  local_1b8 = 0x18;
  local_1af = 0x7673632e;
  local_1ab = 0;
  local_1b7 = (undefined5)s_rankGift_csv_002be0c0._0_8_;
  uStack_1b2 = SUB83(s_rankGift_csv_002be0c0._0_8_,5);
  FUN_00b110ec(&local_1a0,&local_1b8,0,0);
  if ((local_1b8 & 1) != 0) {
    _ZdlPv(local_1a8);
  }
  __s = (void *)((long)&DWORD_0039e51c + param_1);
  memset(__s,0xff,0x8340);
  lVar9 = 0;
                    /* try { // try from 009d00a0 to 00ad00b3 has its CatchHandler @ 009d02bc */
  do {
    uVar7 = FUN_0048791c(&local_1a0);
    if (((uVar7 & 1) == 0) || (iVar6 = FUN_00488558(&local_1a0), iVar6 == 1)) break;
    uVar7 = 0;
    do {
                    /* try { // try from 009d00d8 to 00ad0133 has its CatchHandler @ 009d02c4 */
      iVar6 = FUN_0048793c(&local_1a0,uVar7 & 0xffffffff);
      *(int *)((long)__s + uVar7 * 4) = iVar6;
      if (iVar6 == -1) break;
      bVar5 = uVar7 < 0x14;
      uVar7 = uVar7 + 1;
    } while (bVar5);
    lVar9 = lVar9 + 1;
    __s = (void *)((long)__s + 0x54);
  } while (lVar9 != 400);
  FUN_00488658(&local_1a0);
  local_1b8 = 0x1a;
  local_1aa = 0;
  local_1b7._0_1_ = s_unitlimit_csv_002a5d1b[0];
  local_1b7._1_1_ = s_unitlimit_csv_002a5d1b[1];
  local_1b7._2_1_ = s_unitlimit_csv_002a5d1b[2];
  local_1b7._3_1_ = s_unitlimit_csv_002a5d1b[3];
  local_1b7._4_1_ = s_unitlimit_csv_002a5d1b[4];
  uStack_1b2._0_1_ = s_unitlimit_csv_002a5d1b[5];
  uStack_1b2._1_1_ = s_unitlimit_csv_002a5d1b[6];
  uStack_1b2._2_1_ = s_unitlimit_csv_002a5d1b[7];
  local_1af = (undefined4)s_unitlimit_csv_002a5d1b._8_5_;
  local_1ab = SUB51(s_unitlimit_csv_002a5d1b._8_5_,4);
  FUN_00b110ec(&local_1a0,&local_1b8,0,0);
  if ((local_1b8 & 1) != 0) {
    _ZdlPv(local_1a8);
  }
  pbVar8 = BYTE_ARRAY_003a8dd1 + param_1 + 0xf;
  memset(pbVar8,0xff,0x8ac0);
  lVar9 = 0;
  do {
    uVar7 = FUN_0048791c(&local_1a0);
    if ((uVar7 & 1) != 0) {
      FUN_00488558(&local_1a0);
    }
    uVar7 = 0;
    do {
                    /* try { // try from 009d019c to 00ad01c3 has its CatchHandler @ 009d02c0 */
      iVar6 = FUN_0048793c(&local_1a0,uVar7 & 0xffffffff);
      *(int *)(pbVar8 + uVar7 * 4) = iVar6;
      if (iVar6 == -1) break;
      bVar5 = uVar7 < 9;
      uVar7 = uVar7 + 1;
    } while (bVar5);
    lVar9 = lVar9 + 1;
    pbVar8 = pbVar8 + 0x28;
    if (lVar9 == 0x378) {
      FUN_00488658(&local_1a0);
                    /* try { // try from 009d01c8 to 00ad0277 has its CatchHandler @ 009d02bc */
      pbVar8 = BYTE_ARRAY_003b1a2d + param_1 + 0x23;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&DWORD_003b18f8 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&fde_003b18f0 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b1908 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&QWORD_003b18fc + param_1 + 4) = 0xffffffffffffffff;
      *(undefined8 *)((long)&fde_003b1918 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&QWORD_003b1910 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&QWORD_003b1924 + param_1 + 4) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b1920 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&QWORD_003b1938 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b1930 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b1948 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&fde_003b1940 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b1958 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&QWORD_003b194c + param_1 + 4) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b1965 + param_1 + 3;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&DWORD_003b1960 + param_1) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b1965 + param_1 + 0xb;
      pbVar2 = BYTE_ARRAY_003b1965 + param_1 + 0x13;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b1965 + param_1 + 0x1b;
      pbVar2 = BYTE_ARRAY_003b1965 + param_1 + 0x23;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&DWORD_003b1998 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&fde_003b1990 + param_1) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b19a1 + param_1 + 7;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)(&uleb128_003b19a0 + param_1) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b19a1 + param_1 + 0xf;
      pbVar2 = BYTE_ARRAY_003b19a1 + param_1 + 0x17;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b19a1 + param_1 + 0x1f;
      pbVar2 = BYTE_ARRAY_003b19a1 + param_1 + 0x27;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b19a1 + param_1 + 0x2f;
      pbVar2 = BYTE_ARRAY_003b19a1 + param_1 + 0x37;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b19a1 + param_1 + 0x3f;
      *(undefined8 *)((long)&DWORD_003b19e8 + param_1) = 0xffffffffffffffff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b19f5 + param_1 + 3;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&DWORD_003b19f0 + param_1) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b19f5 + param_1 + 0xb;
      pbVar2 = BYTE_ARRAY_003b19f5 + param_1 + 0x13;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b19f5 + param_1 + 0x1b;
      pbVar2 = BYTE_ARRAY_003b19f5 + param_1 + 0x23;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&DWORD_003b1a28 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b1a20 + param_1) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b1a2d + param_1 + 3;
      pbVar2 = BYTE_ARRAY_003b1a2d + param_1 + 0xb;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b1a2d + param_1 + 0x13;
      pbVar2 = BYTE_ARRAY_003b1a2d + param_1 + 0x1b;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&QWORD_003b18e8 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b18e0 + param_1) = 0xffffffffffffffff;
      puVar3 = PTR_DAT_00c9abb0;
      pbVar8 = BYTE_ARRAY_003b18b1 + param_1 + 0xf;
      *(undefined8 *)((long)&fde_003b18c8 + param_1) = 0xffffffffffffffff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&QWORD_003b18d4 + param_1 + 4) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b18d0 + param_1) = 0xffffffffffffffff;
      puVar4 = 
      PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8;
      *(undefined8 *)((long)&DWORD_003b18a8 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&fde_003b18a0 + param_1) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b18b1 + param_1 + 7;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)(&uleb128_003b18b0 + param_1) = 0xffffffffffffffff;
      local_1a0 = (undefined **)(puVar3 + 0x10);
      local_158 = *(long *)puVar4;
      *(undefined8 *)((long)&local_158 + *(long *)(local_158 + -0x18)) =
           *(undefined8 *)(puVar4 + 0x18);
      local_150[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abc0
                     + 0x10;
      if ((local_110 & 1) != 0) {
        _ZdlPv(local_100);
      }
      _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_150);
      _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_158,puVar4 + 8);
                    /* try { // try from 009d0278 to 00ad02f7 has its CatchHandler @ 009cfe24 */
      _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_e8);
      if ((local_180 & 1) != 0) {
        _ZdlPv(local_170);
      }
      if (local_198 != (void *)0x0) {
        local_190 = local_198;
        _ZdlPv(local_198);
      }
      if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
        __stack_chk_fail();
      }
                    /* catch() { ... } // from try @ 009d00a0 with catch @ 009d02bc
                       catch() { ... } // from try @ 009d01c8 with catch @ 009d02bc */
                    /* catch() { ... } // from try @ 009d019c with catch @ 009d02c0 */
                    /* catch() { ... } // from try @ 009d00d8 with catch @ 009d02c4 */
      return;
    }
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009cfffc"></a> `009cfffc` | `ff 03 07 d1` | sub sp,sp,#0x1c0 | `FALL_THROUGH`
<a id="insn-009d0000"></a> `009d0000` | `fd 7b 18 a9` | stp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-009d0004"></a> `009d0004` | `fc 5f 19 a9` | stp x28,x23,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-009d0008"></a> `009d0008` | `f6 57 1a a9` | stp x22,x21,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-009d000c"></a> `009d000c` | `f4 4f 1b a9` | stp x20,x19,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-009d0010"></a> `009d0010` | `fd 03 06 91` | add x29,sp,#0x180 | `FALL_THROUGH`
<a id="insn-009d0014"></a> `009d0014` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009d0018"></a> `009d0018` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009d001c"></a> `009d001c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d0020"></a> `009d0020` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-009d0024"></a> `009d0024` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009d0028"></a> `009d0028` | `7e df ea 97` | bl 0x00487e20 | `UNCONDITIONAL_CALL`
<a id="insn-009d002c"></a> `009d002c` | `a8 14 00 90` | adrp x8,0xc64000 | `FALL_THROUGH`
<a id="insn-009d0030"></a> `009d0030` | `08 e1 34 91` | add x8,x8,#0xd38 | `FALL_THROUGH`
<a id="insn-009d0034"></a> `009d0034` | `c9 65 8c 52` | mov w9,#0x632e | `FALL_THROUGH`
<a id="insn-009d0038"></a> `009d0038` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009d003c"></a> `009d003c` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-009d0040"></a> `009d0040` | `69 ce ae 72` | movk w9,#0x7673, LSL #16 | `FALL_THROUGH`
<a id="insn-009d0044"></a> `009d0044` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009d0048"></a> `009d0048` | `68 c7 ff d0` | adrp x8,0x2be000 | `FALL_THROUGH`
<a id="insn-009d004c"></a> `009d004c` | `08 01 03 91` | add x8,x8,#0xc0 | `FALL_THROUGH`
<a id="insn-009d0050"></a> `009d0050` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-009d0054"></a> `009d0054` | `e9 13 01 b8` | stur w9,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-009d0058"></a> `009d0058` | `ff 57 00 39` | strb wzr,[sp, #0x15] | `FALL_THROUGH`
<a id="insn-009d005c"></a> `009d005c` | `e8 93 00 f8` | stur x8,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-009d0060"></a> `009d0060` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d0064"></a> `009d0064` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-009d0068"></a> `009d0068` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009d006c"></a> `009d006c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009d0070"></a> `009d0070` | `1f 04 05 94` | bl 0x00b110ec | `UNCONDITIONAL_CALL`
<a id="insn-009d0074"></a> `009d0074` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009d0078"></a> `009d0078` | `68 00 00 36` | tbz w8,#0x0,0x009d0084 | `CONDITIONAL_JUMP`
<a id="insn-009d007c"></a> `009d007c` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009d0080"></a> `009d0080` | `8c 1f 0a 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009d0084"></a> `009d0084` | `68 7a 4e 91` | add x8,x19,#0x39e, LSL #12 | `FALL_THROUGH`
<a id="insn-009d0088"></a> `009d0088` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-009d008c"></a> `009d008c` | `02 68 90 52` | mov w2,#0x8340 | `FALL_THROUGH`
<a id="insn-009d0090"></a> `009d0090` | `14 71 14 91` | add x20,x8,#0x51c | `FALL_THROUGH`
<a id="insn-009d0094"></a> `009d0094` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009d0098"></a> `009d0098` | `fe 1f 0a 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-009d009c"></a> `009d009c` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-009d00a0"></a> `009d00a0` | `05 00 00 14` | b 0x009d00b4 | `UNCONDITIONAL_JUMP`
<a id="insn-009d00a4"></a> `009d00a4` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-009d00a8"></a> `009d00a8` | `94 52 01 91` | add x20,x20,#0x54 | `FALL_THROUGH`
<a id="insn-009d00ac"></a> `009d00ac` | `ff 42 06 f1` | cmp x23,#0x190 | `FALL_THROUGH`
<a id="insn-009d00b0"></a> `009d00b0` | `60 02 00 54` | b.eq 0x009d00fc | `CONDITIONAL_JUMP`
<a id="insn-009d00b4"></a> `009d00b4` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d00b8"></a> `009d00b8` | `19 de ea 97` | bl 0x0048791c | `UNCONDITIONAL_CALL`
<a id="insn-009d00bc"></a> `009d00bc` | `00 02 00 36` | tbz w0,#0x0,0x009d00fc | `CONDITIONAL_JUMP`
<a id="insn-009d00c0"></a> `009d00c0` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d00c4"></a> `009d00c4` | `25 e1 ea 97` | bl 0x00488558 | `UNCONDITIONAL_CALL`
<a id="insn-009d00c8"></a> `009d00c8` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-009d00cc"></a> `009d00cc` | `80 01 00 54` | b.eq 0x009d00fc | `CONDITIONAL_JUMP`
<a id="insn-009d00d0"></a> `009d00d0` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-009d00d4"></a> `009d00d4` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d00d8"></a> `009d00d8` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-009d00dc"></a> `009d00dc` | `18 de ea 97` | bl 0x0048793c | `UNCONDITIONAL_CALL`
<a id="insn-009d00e0"></a> `009d00e0` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-009d00e4"></a> `009d00e4` | `80 7a 35 b8` | str w0,[x20, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-009d00e8"></a> `009d00e8` | `e0 fd ff 54` | b.eq 0x009d00a4 | `CONDITIONAL_JUMP`
<a id="insn-009d00ec"></a> `009d00ec` | `bf 52 00 f1` | cmp x21,#0x14 | `FALL_THROUGH`
<a id="insn-009d00f0"></a> `009d00f0` | `b5 06 00 91` | add x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-009d00f4"></a> `009d00f4` | `03 ff ff 54` | b.cc 0x009d00d4 | `CONDITIONAL_JUMP`
<a id="insn-009d00f8"></a> `009d00f8` | `eb ff ff 17` | b 0x009d00a4 | `UNCONDITIONAL_JUMP`
<a id="insn-009d00fc"></a> `009d00fc` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d0100"></a> `009d0100` | `56 e1 ea 97` | bl 0x00488658 | `UNCONDITIONAL_CALL`
<a id="insn-009d0104"></a> `009d0104` | `a9 c6 ff b0` | adrp x9,0x2a5000 | `FALL_THROUGH`
<a id="insn-009d0108"></a> `009d0108` | `29 6d 34 91` | add x9,x9,#0xd1b | `FALL_THROUGH`
<a id="insn-009d010c"></a> `009d010c` | `48 03 80 52` | mov w8,#0x1a | `FALL_THROUGH`
<a id="insn-009d0110"></a> `009d0110` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-009d0114"></a> `009d0114` | `29 51 40 f8` | ldur x9,[x9, #0x5] | `FALL_THROUGH`
<a id="insn-009d0118"></a> `009d0118` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009d011c"></a> `009d011c` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-009d0120"></a> `009d0120` | `ea 93 00 f8` | stur x10,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-009d0124"></a> `009d0124` | `e9 e3 00 f8` | stur x9,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-009d0128"></a> `009d0128` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d012c"></a> `009d012c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-009d0130"></a> `009d0130` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009d0134"></a> `009d0134` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009d0138"></a> `009d0138` | `ed 03 05 94` | bl 0x00b110ec | `UNCONDITIONAL_CALL`
<a id="insn-009d013c"></a> `009d013c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009d0140"></a> `009d0140` | `68 00 00 36` | tbz w8,#0x0,0x009d014c | `CONDITIONAL_JUMP`
<a id="insn-009d0144"></a> `009d0144` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009d0148"></a> `009d0148` | `5a 1f 0a 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009d014c"></a> `009d014c` | `68 a2 4e 91` | add x8,x19,#0x3a8, LSL #12 | `FALL_THROUGH`
<a id="insn-009d0150"></a> `009d0150` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-009d0154"></a> `009d0154` | `02 58 91 52` | mov w2,#0x8ac0 | `FALL_THROUGH`
<a id="insn-009d0158"></a> `009d0158` | `14 81 37 91` | add x20,x8,#0xde0 | `FALL_THROUGH`
<a id="insn-009d015c"></a> `009d015c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009d0160"></a> `009d0160` | `cc 1f 0a 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-009d0164"></a> `009d0164` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-009d0168"></a> `009d0168` | `05 00 00 14` | b 0x009d017c | `UNCONDITIONAL_JUMP`
<a id="insn-009d016c"></a> `009d016c` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-009d0170"></a> `009d0170` | `94 a2 00 91` | add x20,x20,#0x28 | `FALL_THROUGH`
<a id="insn-009d0174"></a> `009d0174` | `ff e2 0d f1` | cmp x23,#0x378 | `FALL_THROUGH`
<a id="insn-009d0178"></a> `009d0178` | `20 02 00 54` | b.eq 0x009d01bc | `CONDITIONAL_JUMP`
<a id="insn-009d017c"></a> `009d017c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d0180"></a> `009d0180` | `e7 dd ea 97` | bl 0x0048791c | `UNCONDITIONAL_CALL`
<a id="insn-009d0184"></a> `009d0184` | `60 00 00 36` | tbz w0,#0x0,0x009d0190 | `CONDITIONAL_JUMP`
<a id="insn-009d0188"></a> `009d0188` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d018c"></a> `009d018c` | `f3 e0 ea 97` | bl 0x00488558 | `UNCONDITIONAL_CALL`
<a id="insn-009d0190"></a> `009d0190` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-009d0194"></a> `009d0194` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d0198"></a> `009d0198` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-009d019c"></a> `009d019c` | `e8 dd ea 97` | bl 0x0048793c | `UNCONDITIONAL_CALL`
<a id="insn-009d01a0"></a> `009d01a0` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-009d01a4"></a> `009d01a4` | `80 7a 35 b8` | str w0,[x20, x21, LSL #0x2] | `FALL_THROUGH`
<a id="insn-009d01a8"></a> `009d01a8` | `20 fe ff 54` | b.eq 0x009d016c | `CONDITIONAL_JUMP`
<a id="insn-009d01ac"></a> `009d01ac` | `bf 26 00 f1` | cmp x21,#0x9 | `FALL_THROUGH`
<a id="insn-009d01b0"></a> `009d01b0` | `b5 06 00 91` | add x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-009d01b4"></a> `009d01b4` | `03 ff ff 54` | b.cc 0x009d0194 | `CONDITIONAL_JUMP`
<a id="insn-009d01b8"></a> `009d01b8` | `ed ff ff 17` | b 0x009d016c | `UNCONDITIONAL_JUMP`
<a id="insn-009d01bc"></a> `009d01bc` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d01c0"></a> `009d01c0` | `f4 83 00 91` | add x20,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d01c4"></a> `009d01c4` | `25 e1 ea 97` | bl 0x00488658 | `UNCONDITIONAL_CALL`
<a id="insn-009d01c8"></a> `009d01c8` | `e0 e7 07 6f` | movi v0.2D,#-0x1 | `FALL_THROUGH`
<a id="insn-009d01cc"></a> `009d01cc` | `68 c6 4e 91` | add x8,x19,#0x3b1, LSL #12 | `FALL_THROUGH`
<a id="insn-009d01d0"></a> `009d01d0` | `09 00 80 92` | mov x9,#-0x1 | `FALL_THROUGH`
<a id="insn-009d01d4"></a> `009d01d4` | `08 81 22 91` | add x8,x8,#0x8a0 | `FALL_THROUGH`
<a id="insn-009d01d8"></a> `009d01d8` | `55 16 00 d0` | adrp x21,0xc9a000 | `FALL_THROUGH`
<a id="insn-009d01dc"></a> `009d01dc` | `93 22 01 91` | add x19,x20,#0x48 | `FALL_THROUGH`
<a id="insn-009d01e0"></a> `009d01e0` | `09 d9 00 f9` | str x9,[x8, #0x1b0] | `FALL_THROUGH`
<a id="insn-009d01e4"></a> `009d01e4` | `49 16 00 d0` | adrp x9,0xc9a000 | `FALL_THROUGH`
<a id="insn-009d01e8"></a> `009d01e8` | `00 81 02 ad` | stp q0,q0,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-009d01ec"></a> `009d01ec` | `00 81 03 ad` | stp q0,q0,[x8, #0x70] | `FALL_THROUGH`
<a id="insn-009d01f0"></a> `009d01f0` | `00 81 04 ad` | stp q0,q0,[x8, #0x90] | `FALL_THROUGH`
<a id="insn-009d01f4"></a> `009d01f4` | `00 81 05 ad` | stp q0,q0,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-009d01f8"></a> `009d01f8` | `00 81 06 ad` | stp q0,q0,[x8, #0xd0] | `FALL_THROUGH`
<a id="insn-009d01fc"></a> `009d01fc` | `00 81 07 ad` | stp q0,q0,[x8, #0xf0] | `FALL_THROUGH`
<a id="insn-009d0200"></a> `009d0200` | `00 81 08 ad` | stp q0,q0,[x8, #0x110] | `FALL_THROUGH`
<a id="insn-009d0204"></a> `009d0204` | `00 81 09 ad` | stp q0,q0,[x8, #0x130] | `FALL_THROUGH`
<a id="insn-009d0208"></a> `009d0208` | `00 81 0a ad` | stp q0,q0,[x8, #0x150] | `FALL_THROUGH`
<a id="insn-009d020c"></a> `009d020c` | `00 81 0b ad` | stp q0,q0,[x8, #0x170] | `FALL_THROUGH`
<a id="insn-009d0210"></a> `009d0210` | `00 81 0c ad` | stp q0,q0,[x8, #0x190] | `FALL_THROUGH`
<a id="insn-009d0214"></a> `009d0214` | `00 11 80 3d` | str q0,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-009d0218"></a> `009d0218` | `29 d9 45 f9` | ldr x9,[x9, #0xbb0] | `FALL_THROUGH`
<a id="insn-009d021c"></a> `009d021c` | `00 01 01 ad` | stp q0,q0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-009d0220"></a> `009d0220` | `b5 de 45 f9` | ldr x21,[x21, #0xbb8] | `FALL_THROUGH`
<a id="insn-009d0224"></a> `009d0224` | `00 01 00 ad` | stp q0,q0,[x8] | `FALL_THROUGH`
<a id="insn-009d0228"></a> `009d0228` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-009d022c"></a> `009d022c` | `aa 02 40 f9` | ldr x10,[x21] | `FALL_THROUGH`
<a id="insn-009d0230"></a> `009d0230` | `e9 13 00 f9` | str x9,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009d0234"></a> `009d0234` | `a9 0e 40 f9` | ldr x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-009d0238"></a> `009d0238` | `ea 37 00 f9` | str x10,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-009d023c"></a> `009d023c` | `48 81 5e f8` | ldur x8,[x10, #-0x18] | `FALL_THROUGH`
<a id="insn-009d0240"></a> `009d0240` | `69 6a 28 f8` | str x9,[x19, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009d0244"></a> `009d0244` | `48 16 00 d0` | adrp x8,0xc9a000 | `FALL_THROUGH`
<a id="insn-009d0248"></a> `009d0248` | `08 e1 45 f9` | ldr x8,[x8, #0xbc0] | `FALL_THROUGH`
<a id="insn-009d024c"></a> `009d024c` | `e9 c3 42 39` | ldrb w9,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-009d0250"></a> `009d0250` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-009d0254"></a> `009d0254` | `e8 3b 00 f9` | str x8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009d0258"></a> `009d0258` | `69 00 00 36` | tbz w9,#0x0,0x009d0264 | `CONDITIONAL_JUMP`
<a id="insn-009d025c"></a> `009d025c` | `e0 63 40 f9` | ldr x0,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-009d0260"></a> `009d0260` | `14 1f 0a 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009d0264"></a> `009d0264` | `80 42 01 91` | add x0,x20,#0x50 | `FALL_THROUGH`
<a id="insn-009d0268"></a> `009d0268` | `4e 1f 0a 94` | bl 0x00c57fa0 | `UNCONDITIONAL_CALL`
<a id="insn-009d026c"></a> `009d026c` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-009d0270"></a> `009d0270` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009d0274"></a> `009d0274` | `4f 1f 0a 94` | bl 0x00c57fb0 | `UNCONDITIONAL_CALL`
<a id="insn-009d0278"></a> `009d0278` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009d027c"></a> `009d027c` | `00 e1 02 91` | add x0,x8,#0xb8 | `FALL_THROUGH`
<a id="insn-009d0280"></a> `009d0280` | `50 1f 0a 94` | bl 0x00c57fc0 | `UNCONDITIONAL_CALL`
<a id="insn-009d0284"></a> `009d0284` | `e8 03 41 39` | ldrb w8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009d0288"></a> `009d0288` | `68 00 00 36` | tbz w8,#0x0,0x009d0294 | `CONDITIONAL_JUMP`
<a id="insn-009d028c"></a> `009d028c` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009d0290"></a> `009d0290` | `08 1f 0a 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009d0294"></a> `009d0294` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-009d0298"></a> `009d0298` | `60 00 00 b4` | cbz x0,0x009d02a4 | `CONDITIONAL_JUMP`
<a id="insn-009d029c"></a> `009d029c` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009d02a0"></a> `009d02a0` | `04 1f 0a 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009d02a4"></a> `009d02a4` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-009d02a8"></a> `009d02a8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009d02ac"></a> `009d02ac` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009d02b0"></a> `009d02b0` | `61 03 00 54` | b.ne 0x009d031c | `CONDITIONAL_JUMP`
<a id="insn-009d02b4"></a> `009d02b4` | `f4 4f 5b a9` | ldp x20,x19,[sp, #0x1b0] | `FALL_THROUGH`
<a id="insn-009d02b8"></a> `009d02b8` | `f6 57 5a a9` | ldp x22,x21,[sp, #0x1a0] | `FALL_THROUGH`
<a id="insn-009d02bc"></a> `009d02bc` | `fc 5f 59 a9` | ldp x28,x23,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-009d02c0"></a> `009d02c0` | `fd 7b 58 a9` | ldp x29,x30,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-009d02c4"></a> `009d02c4` | `ff 03 07 91` | add sp,sp,#0x1c0 | `FALL_THROUGH`
<a id="insn-009d02c8"></a> `009d02c8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009d031c"></a> `009d031c` | `f1 1e 0a 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009cfffc`](#insn-009cfffc) 範囲 `[['009cfffc', '009d007b']]`
  - `CONDITIONAL_JUMP` [`009d0078`](#insn-009d0078) → [`009d0084`](#insn-009d0084)
  - `FALL_THROUGH` [`009d0078`](#insn-009d0078) → [`009d007c`](#insn-009d007c)
- ブロック [`009d007c`](#insn-009d007c) 範囲 `[['009d007c', '009d0083']]`
  - `FALL_THROUGH` [`009d0080`](#insn-009d0080) → [`009d0084`](#insn-009d0084)
- ブロック [`009d0084`](#insn-009d0084) 範囲 `[['009d0084', '009d009f']]`
  - `FALL_THROUGH` [`009d009c`](#insn-009d009c) → [`009d00a0`](#insn-009d00a0)
- ブロック [`009d00a0`](#insn-009d00a0) 範囲 `[['009d00a0', '009d00a3']]`
  - `UNCONDITIONAL_JUMP` [`009d00a0`](#insn-009d00a0) → [`009d00b4`](#insn-009d00b4)
- ブロック [`009d00a4`](#insn-009d00a4) 範囲 `[['009d00a4', '009d00b3']]`
  - `CONDITIONAL_JUMP` [`009d00b0`](#insn-009d00b0) → [`009d00fc`](#insn-009d00fc)
  - `FALL_THROUGH` [`009d00b0`](#insn-009d00b0) → [`009d00b4`](#insn-009d00b4)
- ブロック [`009d00b4`](#insn-009d00b4) 範囲 `[['009d00b4', '009d00bf']]`
  - `CONDITIONAL_JUMP` [`009d00bc`](#insn-009d00bc) → [`009d00fc`](#insn-009d00fc)
  - `FALL_THROUGH` [`009d00bc`](#insn-009d00bc) → [`009d00c0`](#insn-009d00c0)
- ブロック [`009d00c0`](#insn-009d00c0) 範囲 `[['009d00c0', '009d00cf']]`
  - `CONDITIONAL_JUMP` [`009d00cc`](#insn-009d00cc) → [`009d00fc`](#insn-009d00fc)
  - `FALL_THROUGH` [`009d00cc`](#insn-009d00cc) → [`009d00d0`](#insn-009d00d0)
- ブロック [`009d00d0`](#insn-009d00d0) 範囲 `[['009d00d0', '009d00d3']]`
  - `FALL_THROUGH` [`009d00d0`](#insn-009d00d0) → [`009d00d4`](#insn-009d00d4)
- ブロック [`009d00d4`](#insn-009d00d4) 範囲 `[['009d00d4', '009d00d7']]`
  - `FALL_THROUGH` [`009d00d4`](#insn-009d00d4) → [`009d00d8`](#insn-009d00d8)
- ブロック [`009d00d8`](#insn-009d00d8) 範囲 `[['009d00d8', '009d00eb']]`
  - `CONDITIONAL_JUMP` [`009d00e8`](#insn-009d00e8) → [`009d00a4`](#insn-009d00a4)
  - `FALL_THROUGH` [`009d00e8`](#insn-009d00e8) → [`009d00ec`](#insn-009d00ec)
- ブロック [`009d00ec`](#insn-009d00ec) 範囲 `[['009d00ec', '009d00f7']]`
  - `CONDITIONAL_JUMP` [`009d00f4`](#insn-009d00f4) → [`009d00d4`](#insn-009d00d4)
  - `FALL_THROUGH` [`009d00f4`](#insn-009d00f4) → [`009d00f8`](#insn-009d00f8)
- ブロック [`009d00f8`](#insn-009d00f8) 範囲 `[['009d00f8', '009d00fb']]`
  - `UNCONDITIONAL_JUMP` [`009d00f8`](#insn-009d00f8) → [`009d00a4`](#insn-009d00a4)
- ブロック [`009d00fc`](#insn-009d00fc) 範囲 `[['009d00fc', '009d0143']]`
  - `CONDITIONAL_JUMP` [`009d0140`](#insn-009d0140) → [`009d014c`](#insn-009d014c)
  - `FALL_THROUGH` [`009d0140`](#insn-009d0140) → [`009d0144`](#insn-009d0144)
- ブロック [`009d0144`](#insn-009d0144) 範囲 `[['009d0144', '009d014b']]`
  - `FALL_THROUGH` [`009d0148`](#insn-009d0148) → [`009d014c`](#insn-009d014c)
- ブロック [`009d014c`](#insn-009d014c) 範囲 `[['009d014c', '009d016b']]`
  - `UNCONDITIONAL_JUMP` [`009d0168`](#insn-009d0168) → [`009d017c`](#insn-009d017c)
- ブロック [`009d016c`](#insn-009d016c) 範囲 `[['009d016c', '009d017b']]`
  - `CONDITIONAL_JUMP` [`009d0178`](#insn-009d0178) → [`009d01bc`](#insn-009d01bc)
  - `FALL_THROUGH` [`009d0178`](#insn-009d0178) → [`009d017c`](#insn-009d017c)
- ブロック [`009d017c`](#insn-009d017c) 範囲 `[['009d017c', '009d0187']]`
  - `CONDITIONAL_JUMP` [`009d0184`](#insn-009d0184) → [`009d0190`](#insn-009d0190)
  - `FALL_THROUGH` [`009d0184`](#insn-009d0184) → [`009d0188`](#insn-009d0188)
- ブロック [`009d0188`](#insn-009d0188) 範囲 `[['009d0188', '009d018f']]`
  - `FALL_THROUGH` [`009d018c`](#insn-009d018c) → [`009d0190`](#insn-009d0190)
- ブロック [`009d0190`](#insn-009d0190) 範囲 `[['009d0190', '009d0193']]`
  - `FALL_THROUGH` [`009d0190`](#insn-009d0190) → [`009d0194`](#insn-009d0194)
- ブロック [`009d0194`](#insn-009d0194) 範囲 `[['009d0194', '009d019b']]`
  - `FALL_THROUGH` [`009d0198`](#insn-009d0198) → [`009d019c`](#insn-009d019c)
- ブロック [`009d019c`](#insn-009d019c) 範囲 `[['009d019c', '009d01ab']]`
  - `CONDITIONAL_JUMP` [`009d01a8`](#insn-009d01a8) → [`009d016c`](#insn-009d016c)
  - `FALL_THROUGH` [`009d01a8`](#insn-009d01a8) → [`009d01ac`](#insn-009d01ac)
- ブロック [`009d01ac`](#insn-009d01ac) 範囲 `[['009d01ac', '009d01b7']]`
  - `CONDITIONAL_JUMP` [`009d01b4`](#insn-009d01b4) → [`009d0194`](#insn-009d0194)
  - `FALL_THROUGH` [`009d01b4`](#insn-009d01b4) → [`009d01b8`](#insn-009d01b8)
- ブロック [`009d01b8`](#insn-009d01b8) 範囲 `[['009d01b8', '009d01bb']]`
  - `UNCONDITIONAL_JUMP` [`009d01b8`](#insn-009d01b8) → [`009d016c`](#insn-009d016c)
- ブロック [`009d01bc`](#insn-009d01bc) 範囲 `[['009d01bc', '009d01c7']]`
  - `FALL_THROUGH` [`009d01c4`](#insn-009d01c4) → [`009d01c8`](#insn-009d01c8)
- ブロック [`009d01c8`](#insn-009d01c8) 範囲 `[['009d01c8', '009d025b']]`
  - `CONDITIONAL_JUMP` [`009d0258`](#insn-009d0258) → [`009d0264`](#insn-009d0264)
  - `FALL_THROUGH` [`009d0258`](#insn-009d0258) → [`009d025c`](#insn-009d025c)
- ブロック [`009d025c`](#insn-009d025c) 範囲 `[['009d025c', '009d0263']]`
  - `FALL_THROUGH` [`009d0260`](#insn-009d0260) → [`009d0264`](#insn-009d0264)
- ブロック [`009d0264`](#insn-009d0264) 範囲 `[['009d0264', '009d0277']]`
  - `FALL_THROUGH` [`009d0274`](#insn-009d0274) → [`009d0278`](#insn-009d0278)
- ブロック [`009d0278`](#insn-009d0278) 範囲 `[['009d0278', '009d028b']]`
  - `CONDITIONAL_JUMP` [`009d0288`](#insn-009d0288) → [`009d0294`](#insn-009d0294)
  - `FALL_THROUGH` [`009d0288`](#insn-009d0288) → [`009d028c`](#insn-009d028c)
- ブロック [`009d028c`](#insn-009d028c) 範囲 `[['009d028c', '009d0293']]`
  - `FALL_THROUGH` [`009d0290`](#insn-009d0290) → [`009d0294`](#insn-009d0294)
- ブロック [`009d0294`](#insn-009d0294) 範囲 `[['009d0294', '009d029b']]`
  - `CONDITIONAL_JUMP` [`009d0298`](#insn-009d0298) → [`009d02a4`](#insn-009d02a4)
  - `FALL_THROUGH` [`009d0298`](#insn-009d0298) → [`009d029c`](#insn-009d029c)
- ブロック [`009d029c`](#insn-009d029c) 範囲 `[['009d029c', '009d02a3']]`
  - `FALL_THROUGH` [`009d02a0`](#insn-009d02a0) → [`009d02a4`](#insn-009d02a4)
- ブロック [`009d02a4`](#insn-009d02a4) 範囲 `[['009d02a4', '009d02b3']]`
  - `CONDITIONAL_JUMP` [`009d02b0`](#insn-009d02b0) → [`009d031c`](#insn-009d031c)
  - `FALL_THROUGH` [`009d02b0`](#insn-009d02b0) → [`009d02b4`](#insn-009d02b4)
- ブロック [`009d02b4`](#insn-009d02b4) 範囲 `[['009d02b4', '009d02bb']]`
  - `FALL_THROUGH` [`009d02b8`](#insn-009d02b8) → [`009d02bc`](#insn-009d02bc)
- ブロック [`009d02bc`](#insn-009d02bc) 範囲 `[['009d02bc', '009d02bf']]`
  - `FALL_THROUGH` [`009d02bc`](#insn-009d02bc) → [`009d02c0`](#insn-009d02c0)
- ブロック [`009d02c0`](#insn-009d02c0) 範囲 `[['009d02c0', '009d02c3']]`
  - `FALL_THROUGH` [`009d02c0`](#insn-009d02c0) → [`009d02c4`](#insn-009d02c4)
- ブロック [`009d02c4`](#insn-009d02c4) 範囲 `[['009d02c4', '009d02cb']]`
- ブロック [`009d031c`](#insn-009d031c) 範囲 `[['009d031c', '009d031f']]`

## 命令位置別の参照

- [`009d0000`](#insn-009d0000) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0004`](#insn-009d0004) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0008`](#insn-009d0008) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d000c`](#insn-009d000c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0024`](#insn-009d0024) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0028`](#insn-009d0028) → [`00487e20`](../00487/00487e20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00487e20` · 推定シンボル `None` · 推定型 `None`
- [`009d0038`](#insn-009d0038) → `00c64d38`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009d0038`](#insn-009d0038) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0044`](#insn-009d0044) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0050`](#insn-009d0050) → `002be0c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`009d0054`](#insn-009d0054) → `Stack[-0x1af]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0058`](#insn-009d0058) → `Stack[-0x1ab]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d005c`](#insn-009d005c) → `Stack[-0x1b7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0070`](#insn-009d0070) → [`00b110ec`](../00b11/00b110ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b110ec` · 推定シンボル `None` · 推定型 `None`
- [`009d0074`](#insn-009d0074) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0078`](#insn-009d0078) → [`009d0084`](#insn-009d0084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d007c`](#insn-009d007c) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0080`](#insn-009d0080) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009d0098`](#insn-009d0098) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`009d00a0`](#insn-009d00a0) → [`009d00b4`](#insn-009d00b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d00b0`](#insn-009d00b0) → [`009d00fc`](#insn-009d00fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d00b8`](#insn-009d00b8) → [`0048791c`](../00487/0048791c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048791c` · 推定シンボル `None` · 推定型 `None`
- [`009d00bc`](#insn-009d00bc) → [`009d00fc`](#insn-009d00fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d00c4`](#insn-009d00c4) → [`00488558`](../00488/00488558.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488558` · 推定シンボル `None` · 推定型 `None`
- [`009d00cc`](#insn-009d00cc) → [`009d00fc`](#insn-009d00fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d00dc`](#insn-009d00dc) → [`0048793c`](../00487/0048793c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048793c` · 推定シンボル `None` · 推定型 `None`
- [`009d00e4`](#insn-009d00e4) → `0039e51c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`009d00e8`](#insn-009d00e8) → [`009d00a4`](#insn-009d00a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d00f4`](#insn-009d00f4) → [`009d00d4`](#insn-009d00d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d00f8`](#insn-009d00f8) → [`009d00a4`](#insn-009d00a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0100`](#insn-009d0100) → [`00488658`](../00488/00488658.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488658` · 推定シンボル `None` · 推定型 `None`
- [`009d0110`](#insn-009d0110) → `002a5d1b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`009d0114`](#insn-009d0114) → `002a5d20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`009d0118`](#insn-009d0118) → `Stack[-0x1b8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d011c`](#insn-009d011c) → `Stack[-0x1aa]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0120`](#insn-009d0120) → `Stack[-0x1b7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0124`](#insn-009d0124) → `Stack[-0x1b2]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0138`](#insn-009d0138) → [`00b110ec`](../00b11/00b110ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b110ec` · 推定シンボル `None` · 推定型 `None`
- [`009d013c`](#insn-009d013c) → `Stack[-0x1b8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0140`](#insn-009d0140) → [`009d014c`](#insn-009d014c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0144`](#insn-009d0144) → `Stack[-0x1a8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0148`](#insn-009d0148) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009d0160`](#insn-009d0160) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`009d0168`](#insn-009d0168) → [`009d017c`](#insn-009d017c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0178`](#insn-009d0178) → [`009d01bc`](#insn-009d01bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0180`](#insn-009d0180) → [`0048791c`](../00487/0048791c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048791c` · 推定シンボル `None` · 推定型 `None`
- [`009d0184`](#insn-009d0184) → [`009d0190`](#insn-009d0190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d018c`](#insn-009d018c) → [`00488558`](../00488/00488558.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488558` · 推定シンボル `None` · 推定型 `None`
- [`009d019c`](#insn-009d019c) → [`0048793c`](../00487/0048793c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0048793c` · 推定シンボル `None` · 推定型 `None`
- [`009d01a4`](#insn-009d01a4) → `003a8de0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`009d01a8`](#insn-009d01a8) → [`009d016c`](#insn-009d016c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d01b4`](#insn-009d01b4) → [`009d0194`](#insn-009d0194) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d01b8`](#insn-009d01b8) → [`009d016c`](#insn-009d016c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d01c4`](#insn-009d01c4) → [`00488658`](../00488/00488658.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00488658` · 推定シンボル `None` · 推定型 `None`
- [`009d01e0`](#insn-009d01e0) → `003b1a50`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[47]`
- [`009d01e8`](#insn-009d01e8) → `003b18f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_003b18f0` · 推定型 `dword`
- [`009d01e8`](#insn-009d01e8) → `003b1900`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`009d01ec`](#insn-009d01ec) → `003b1910`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`009d01ec`](#insn-009d01ec) → `003b1920`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`009d01f0`](#insn-009d01f0) → `003b1930`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`009d01f0`](#insn-009d01f0) → `003b1940`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_003b1940` · 推定型 `dword`
- [`009d01f4`](#insn-009d01f4) → `003b1950`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`009d01f4`](#insn-009d01f4) → `003b1960`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`009d01f8`](#insn-009d01f8) → `003b1970`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[43]`
- [`009d01f8`](#insn-009d01f8) → `003b1980`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[43]`
- [`009d01fc`](#insn-009d01fc) → `003b1990`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_003b1990` · 推定型 `dword`
- [`009d01fc`](#insn-009d01fc) → `003b19a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`009d0200`](#insn-009d0200) → `003b19b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[67]`
- [`009d0200`](#insn-009d0200) → `003b19c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[67]`
- [`009d0204`](#insn-009d0204) → `003b19d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[67]`
- [`009d0204`](#insn-009d0204) → `003b19e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[67]`
- [`009d0208`](#insn-009d0208) → `003b19f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`009d0208`](#insn-009d0208) → `003b1a00`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`009d020c`](#insn-009d020c) → `003b1a10`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`009d020c`](#insn-009d020c) → `003b1a20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`009d0210`](#insn-009d0210) → `003b1a30`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[47]`
- [`009d0210`](#insn-009d0210) → `003b1a40`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[47]`
- [`009d0214`](#insn-009d0214) → `003b18e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`009d0218`](#insn-009d0218) → `00c9abb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009d021c`](#insn-009d021c) → `003b18c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`009d021c`](#insn-009d021c) → `003b18d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`009d0220`](#insn-009d0220) → `00c9abb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009d0224`](#insn-009d0224) → `003b18a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_003b18a0` · 推定型 `dword`
- [`009d0224`](#insn-009d0224) → `003b18b0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`009d022c`](#insn-009d022c) → `00c93200`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`009d0230`](#insn-009d0230) → `00c65818`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`009d0230`](#insn-009d0230) → `Stack[-0x1a0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0234`](#insn-009d0234) → `00c93218`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`009d0238`](#insn-009d0238) → `00c91010`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009d0238`](#insn-009d0238) → `Stack[-0x158]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d023c`](#insn-009d023c) → `00c90ff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`009d0240`](#insn-009d0240) → `00c91038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009d0248`](#insn-009d0248) → `00c9abc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009d024c`](#insn-009d024c) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0254`](#insn-009d0254) → `00c90c08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`009d0254`](#insn-009d0254) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0258`](#insn-009d0258) → [`009d0264`](#insn-009d0264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d025c`](#insn-009d025c) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0260`](#insn-009d0260) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009d0268`](#insn-009d0268) → [`00c57fa0`](../00c57/00c57fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fa0` · 推定シンボル `None` · 推定型 `None`
- [`009d026c`](#insn-009d026c) → `00c93208`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`009d0274`](#insn-009d0274) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`
- [`009d0280`](#insn-009d0280) → [`00c57fc0`](../00c57/00c57fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fc0` · 推定シンボル `None` · 推定型 `None`
- [`009d0284`](#insn-009d0284) → `Stack[-0x180]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0288`](#insn-009d0288) → [`009d0294`](#insn-009d0294) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d028c`](#insn-009d028c) → `Stack[-0x170]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0290`](#insn-009d0290) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009d0294`](#insn-009d0294) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d0298`](#insn-009d0298) → [`009d02a4`](#insn-009d02a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d029c`](#insn-009d029c) → `Stack[-0x190]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d02a0`](#insn-009d02a0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009d02a8`](#insn-009d02a8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d02b0`](#insn-009d02b0) → [`009d031c`](#insn-009d031c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d02b4`](#insn-009d02b4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d02b8`](#insn-009d02b8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d02bc`](#insn-009d02bc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d02c0`](#insn-009d02c0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009d031c`](#insn-009d031c) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009d0000`](#insn-009d0000)

~~~json
{
  "source": "009d0000",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0004`](#insn-009d0004)

~~~json
{
  "source": "009d0004",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0008`](#insn-009d0008)

~~~json
{
  "source": "009d0008",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d000c`](#insn-009d000c)

~~~json
{
  "source": "009d000c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0024`](#insn-009d0024)

~~~json
{
  "source": "009d0024",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0028`](#insn-009d0028)

~~~json
{
  "source": "009d0028",
  "target": "00487e20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d0038`](#insn-009d0038)

~~~json
{
  "source": "009d0038",
  "target": "00c64d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c64d38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009d0038`](#insn-009d0038)

~~~json
{
  "source": "009d0038",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0044`](#insn-009d0044)

~~~json
{
  "source": "009d0044",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0050`](#insn-009d0050)

~~~json
{
  "source": "009d0050",
  "target": "002be0c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be0c0",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "72616e6b476966742e63737600",
  "capture_start": "002be0c0",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d0054`](#insn-009d0054)

~~~json
{
  "source": "009d0054",
  "target": "Stack[-0x1af]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0058`](#insn-009d0058)

~~~json
{
  "source": "009d0058",
  "target": "Stack[-0x1ab]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d005c`](#insn-009d005c)

~~~json
{
  "source": "009d005c",
  "target": "Stack[-0x1b7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0070`](#insn-009d0070)

~~~json
{
  "source": "009d0070",
  "target": "00b110ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d0074`](#insn-009d0074)

~~~json
{
  "source": "009d0074",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0078`](#insn-009d0078)

~~~json
{
  "source": "009d0078",
  "target": "009d0084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d007c`](#insn-009d007c)

~~~json
{
  "source": "009d007c",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0080`](#insn-009d0080)

~~~json
{
  "source": "009d0080",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d0098`](#insn-009d0098)

~~~json
{
  "source": "009d0098",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d00a0`](#insn-009d00a0)

~~~json
{
  "source": "009d00a0",
  "target": "009d00b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d00b0`](#insn-009d00b0)

~~~json
{
  "source": "009d00b0",
  "target": "009d00fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d00b8`](#insn-009d00b8)

~~~json
{
  "source": "009d00b8",
  "target": "0048791c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d00bc`](#insn-009d00bc)

~~~json
{
  "source": "009d00bc",
  "target": "009d00fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d00c4`](#insn-009d00c4)

~~~json
{
  "source": "009d00c4",
  "target": "00488558",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d00cc`](#insn-009d00cc)

~~~json
{
  "source": "009d00cc",
  "target": "009d00fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d00dc`](#insn-009d00dc)

~~~json
{
  "source": "009d00dc",
  "target": "0048793c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d00e4`](#insn-009d00e4)

~~~json
{
  "source": "009d00e4",
  "target": "0039e51c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039e51c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30dc5100",
  "capture_start": "0039e51c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d00e8`](#insn-009d00e8)

~~~json
{
  "source": "009d00e8",
  "target": "009d00a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d00f4`](#insn-009d00f4)

~~~json
{
  "source": "009d00f4",
  "target": "009d00d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d00f8`](#insn-009d00f8)

~~~json
{
  "source": "009d00f8",
  "target": "009d00a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0100`](#insn-009d0100)

~~~json
{
  "source": "009d0100",
  "target": "00488658",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d0110`](#insn-009d0110)

~~~json
{
  "source": "009d0110",
  "target": "002a5d1b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a5d1b",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "756e69746c696d69742e63737600",
  "capture_start": "002a5d1b",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d0114`](#insn-009d0114)

~~~json
{
  "source": "009d0114",
  "target": "002a5d20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a5d1b",
  "offset": 5,
  "size": 14,
  "datatype": "string",
  "bytes": "756e69746c696d69742e63737600",
  "capture_start": "002a5d1b",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d0118`](#insn-009d0118)

~~~json
{
  "source": "009d0118",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d011c`](#insn-009d011c)

~~~json
{
  "source": "009d011c",
  "target": "Stack[-0x1aa]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0120`](#insn-009d0120)

~~~json
{
  "source": "009d0120",
  "target": "Stack[-0x1b7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0124`](#insn-009d0124)

~~~json
{
  "source": "009d0124",
  "target": "Stack[-0x1b2]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0138`](#insn-009d0138)

~~~json
{
  "source": "009d0138",
  "target": "00b110ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d013c`](#insn-009d013c)

~~~json
{
  "source": "009d013c",
  "target": "Stack[-0x1b8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0140`](#insn-009d0140)

~~~json
{
  "source": "009d0140",
  "target": "009d014c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0144`](#insn-009d0144)

~~~json
{
  "source": "009d0144",
  "target": "Stack[-0x1a8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0148`](#insn-009d0148)

~~~json
{
  "source": "009d0148",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d0160`](#insn-009d0160)

~~~json
{
  "source": "009d0160",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d0168`](#insn-009d0168)

~~~json
{
  "source": "009d0168",
  "target": "009d017c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0178`](#insn-009d0178)

~~~json
{
  "source": "009d0178",
  "target": "009d01bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0180`](#insn-009d0180)

~~~json
{
  "source": "009d0180",
  "target": "0048791c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d0184`](#insn-009d0184)

~~~json
{
  "source": "009d0184",
  "target": "009d0190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d018c`](#insn-009d018c)

~~~json
{
  "source": "009d018c",
  "target": "00488558",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d019c`](#insn-009d019c)

~~~json
{
  "source": "009d019c",
  "target": "0048793c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d01a4`](#insn-009d01a4)

~~~json
{
  "source": "009d01a4",
  "target": "003a8de0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003a8dd1",
  "offset": 15,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "003a8dd1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`009d01a8`](#insn-009d01a8)

~~~json
{
  "source": "009d01a8",
  "target": "009d016c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d01b4`](#insn-009d01b4)

~~~json
{
  "source": "009d01b4",
  "target": "009d0194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d01b8`](#insn-009d01b8)

~~~json
{
  "source": "009d01b8",
  "target": "009d016c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d01c4`](#insn-009d01c4)

~~~json
{
  "source": "009d01c4",
  "target": "00488658",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d01e0`](#insn-009d01e0)

~~~json
{
  "source": "009d01e0",
  "target": "003b1a50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b1a2d",
  "offset": 35,
  "size": 47,
  "datatype": "byte[47]",
  "bytes": "440e304c0c1d309302940495089e0a9d0c0a024c0c1f304c0e00d3d4d5dedd44",
  "capture_start": "003b1a2d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`009d01e8`](#insn-009d01e8)

~~~json
{
  "source": "009d01e8",
  "target": "003b18f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b18f0",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "003b18f0",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d01e8`](#insn-009d01e8)

~~~json
{
  "source": "009d01e8",
  "target": "003b1900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b18fc",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "003b18fc",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d01ec`](#insn-009d01ec)

~~~json
{
  "source": "009d01ec",
  "target": "003b1910",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b1910",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "1c00000000000000",
  "capture_start": "003b1910",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d01ec`](#insn-009d01ec)

~~~json
{
  "source": "009d01ec",
  "target": "003b1920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b1920",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "88726800",
  "capture_start": "003b1920",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d01f0`](#insn-009d01f0)

~~~json
{
  "source": "009d01f0",
  "target": "003b1930",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b1930",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "80e20600",
  "capture_start": "003b1930",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d01f0`](#insn-009d01f0)

~~~json
{
  "source": "009d01f0",
  "target": "003b1940",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b1940",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "003b1940",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d01f4`](#insn-009d01f4)

~~~json
{
  "source": "009d01f4",
  "target": "003b1950",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b194c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1400000000000000",
  "capture_start": "003b194c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d01f4`](#insn-009d01f4)

~~~json
{
  "source": "009d01f4",
  "target": "003b1960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b1960",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "d8000000",
  "capture_start": "003b1960",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d01f8`](#insn-009d01f8)

~~~json
{
  "source": "009d01f8",
  "target": "003b1970",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b1965",
  "offset": 11,
  "size": 43,
  "datatype": "byte[43]",
  "bytes": "580e40500c1d3093029404950696089e0a9d0c0548100a028c0c1f40500e00d3",
  "capture_start": "003b1965",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`009d01f8`](#insn-009d01f8)

~~~json
{
  "source": "009d01f8",
  "target": "003b1980",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b1965",
  "offset": 27,
  "size": 43,
  "datatype": "byte[43]",
  "bytes": "580e40500c1d3093029404950696089e0a9d0c0548100a028c0c1f40500e00d3",
  "capture_start": "003b1965",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`009d01fc`](#insn-009d01fc)

~~~json
{
  "source": "009d01fc",
  "target": "003b1990",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b1990",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "50000000",
  "capture_start": "003b1990",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d01fc`](#insn-009d01fc)

~~~json
{
  "source": "009d01fc",
  "target": "003b19a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b19a0",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "003b19a0",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d0200`](#insn-009d0200)

~~~json
{
  "source": "009d0200",
  "target": "003b19b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b19a1",
  "offset": 15,
  "size": 67,
  "datatype": "byte[67]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0340010c1f50",
  "capture_start": "003b19a1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`009d0200`](#insn-009d0200)

~~~json
{
  "source": "009d0200",
  "target": "003b19c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b19a1",
  "offset": 31,
  "size": 67,
  "datatype": "byte[67]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0340010c1f50",
  "capture_start": "003b19a1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`009d0204`](#insn-009d0204)

~~~json
{
  "source": "009d0204",
  "target": "003b19d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b19a1",
  "offset": 47,
  "size": 67,
  "datatype": "byte[67]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0340010c1f50",
  "capture_start": "003b19a1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`009d0204`](#insn-009d0204)

~~~json
{
  "source": "009d0204",
  "target": "003b19e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b19a1",
  "offset": 63,
  "size": 67,
  "datatype": "byte[67]",
  "bytes": "440e50540c1d509302940495069608970a980c99109e129d140a0340010c1f50",
  "capture_start": "003b19a1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`009d0208`](#insn-009d0208)

~~~json
{
  "source": "009d0208",
  "target": "003b19f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b19f0",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "28010000",
  "capture_start": "003b19f0",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d0208`](#insn-009d0208)

~~~json
{
  "source": "009d0208",
  "target": "003b1a00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b19f5",
  "offset": 11,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e40500c1d409302940495069608970c9e0e9d100300010c1f40500e00d3d4",
  "capture_start": "003b19f5",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`009d020c`](#insn-009d020c)

~~~json
{
  "source": "009d020c",
  "target": "003b1a10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b19f5",
  "offset": 27,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e40500c1d409302940495069608970c9e0e9d100300010c1f40500e00d3d4",
  "capture_start": "003b19f5",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`009d020c`](#insn-009d020c)

~~~json
{
  "source": "009d020c",
  "target": "003b1a20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b1a20",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "70e30600",
  "capture_start": "003b1a20",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d0210`](#insn-009d0210)

~~~json
{
  "source": "009d0210",
  "target": "003b1a30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b1a2d",
  "offset": 3,
  "size": 47,
  "datatype": "byte[47]",
  "bytes": "440e304c0c1d309302940495089e0a9d0c0a024c0c1f304c0e00d3d4d5dedd44",
  "capture_start": "003b1a2d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`009d0210`](#insn-009d0210)

~~~json
{
  "source": "009d0210",
  "target": "003b1a40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b1a2d",
  "offset": 19,
  "size": 47,
  "datatype": "byte[47]",
  "bytes": "440e304c0c1d309302940495089e0a9d0c0a024c0c1f304c0e00d3d4d5dedd44",
  "capture_start": "003b1a2d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`009d0214`](#insn-009d0214)

~~~json
{
  "source": "009d0214",
  "target": "003b18e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b18e0",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30e20600",
  "capture_start": "003b18e0",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d0218`](#insn-009d0218)

~~~json
{
  "source": "009d0218",
  "target": "00c9abb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abb0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009d021c`](#insn-009d021c)

~~~json
{
  "source": "009d021c",
  "target": "003b18c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b18b1",
  "offset": 15,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "4c0e20480c1d2093049e069d084c0c1f20480e00d3dedd",
  "capture_start": "003b18b1",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d021c`](#insn-009d021c)

~~~json
{
  "source": "009d021c",
  "target": "003b18d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b18d0",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "2c686800",
  "capture_start": "003b18d0",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d0220`](#insn-009d0220)

~~~json
{
  "source": "009d0220",
  "target": "00c9abb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abb8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009d0224`](#insn-009d0224)

~~~json
{
  "source": "009d0224",
  "target": "003b18a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b18a0",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "24000000",
  "capture_start": "003b18a0",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d0224`](#insn-009d0224)

~~~json
{
  "source": "009d0224",
  "target": "003b18b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003b18b0",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "003b18b0",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d022c`](#insn-009d022c)

~~~json
{
  "source": "009d022c",
  "target": "00c93200",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93200",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009d0230`](#insn-009d0230)

~~~json
{
  "source": "009d0230",
  "target": "00c65818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009d0230`](#insn-009d0230)

~~~json
{
  "source": "009d0230",
  "target": "Stack[-0x1a0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0234`](#insn-009d0234)

~~~json
{
  "source": "009d0234",
  "target": "00c93218",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93218",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009d0238`](#insn-009d0238)

~~~json
{
  "source": "009d0238",
  "target": "00c91010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91010",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009d0238`](#insn-009d0238)

~~~json
{
  "source": "009d0238",
  "target": "Stack[-0x158]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d023c`](#insn-009d023c)

~~~json
{
  "source": "009d023c",
  "target": "00c90ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90ff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c90ff8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009d0240`](#insn-009d0240)

~~~json
{
  "source": "009d0240",
  "target": "00c91038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91038",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009d0248`](#insn-009d0248)

~~~json
{
  "source": "009d0248",
  "target": "00c9abc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009d024c`](#insn-009d024c)

~~~json
{
  "source": "009d024c",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0254`](#insn-009d0254)

~~~json
{
  "source": "009d0254",
  "target": "00c90c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90bf8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`009d0254`](#insn-009d0254)

~~~json
{
  "source": "009d0254",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0258`](#insn-009d0258)

~~~json
{
  "source": "009d0258",
  "target": "009d0264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d025c`](#insn-009d025c)

~~~json
{
  "source": "009d025c",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0260`](#insn-009d0260)

~~~json
{
  "source": "009d0260",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d0268`](#insn-009d0268)

~~~json
{
  "source": "009d0268",
  "target": "00c57fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d026c`](#insn-009d026c)

~~~json
{
  "source": "009d026c",
  "target": "00c93208",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93208",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009d0274`](#insn-009d0274)

~~~json
{
  "source": "009d0274",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d0280`](#insn-009d0280)

~~~json
{
  "source": "009d0280",
  "target": "00c57fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d0284`](#insn-009d0284)

~~~json
{
  "source": "009d0284",
  "target": "Stack[-0x180]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0288`](#insn-009d0288)

~~~json
{
  "source": "009d0288",
  "target": "009d0294",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d028c`](#insn-009d028c)

~~~json
{
  "source": "009d028c",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0290`](#insn-009d0290)

~~~json
{
  "source": "009d0290",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d0294`](#insn-009d0294)

~~~json
{
  "source": "009d0294",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d0298`](#insn-009d0298)

~~~json
{
  "source": "009d0298",
  "target": "009d02a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d029c`](#insn-009d029c)

~~~json
{
  "source": "009d029c",
  "target": "Stack[-0x190]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d02a0`](#insn-009d02a0)

~~~json
{
  "source": "009d02a0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009d02a8`](#insn-009d02a8)

~~~json
{
  "source": "009d02a8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d02b0`](#insn-009d02b0)

~~~json
{
  "source": "009d02b0",
  "target": "009d031c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d02b4`](#insn-009d02b4)

~~~json
{
  "source": "009d02b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d02b8`](#insn-009d02b8)

~~~json
{
  "source": "009d02b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d02bc`](#insn-009d02bc)

~~~json
{
  "source": "009d02bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d02c0`](#insn-009d02c0)

~~~json
{
  "source": "009d02c0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009d031c`](#insn-009d031c)

~~~json
{
  "source": "009d031c",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
