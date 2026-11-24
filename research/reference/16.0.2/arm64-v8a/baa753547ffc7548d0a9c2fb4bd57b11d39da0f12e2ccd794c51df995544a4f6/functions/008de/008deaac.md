# 008deaac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `008dea58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/008de/008dea58.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0052.md#compare-2ee39079a61c7bc71db79e0bedf3892a)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `008dfa58`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/008df/008dfa58.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0054.md#compare-143750f4f190383c46bcfdc05a4f316d)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008deaac",
  "name": "FUN_008deaac",
  "size": 2496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d65bac5cb592f0afb4886e5bcd17cc8837d7db9cb69926cb4d825527a89600b2",
  "source_text_sha256": "d65bac5cb592f0afb4886e5bcd17cc8837d7db9cb69926cb4d825527a89600b2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008deaac",
        "008df46b"
      ]
    ],
    "bytes_sha256": "191ba998537aa0654a06fe40ef28b55c0ef35f78ae7c486f94d439f294800cfc",
    "instruction_count": 624,
    "instruction_bytes": 2496,
    "body_bytes": 2496,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00859bb0](../00859/00859bb0.md)

## 呼び出し先

- [00467ba0](../00467/00467ba0.md)
- [00468c1c](../00468/00468c1c.md)
- [00468ca0](../00468/00468ca0.md)
- [00468fc8](../00468/00468fc8.md)
- [00469c44](../00469/00469c44.md)
- [0046af4c](../0046a/0046af4c.md)
- [0046ca04](../0046c/0046ca04.md)
- [0046cac4](../0046c/0046cac4.md)
- [0046d9b4](../0046d/0046d9b4.md)
- [0046d9ec](../0046d/0046d9ec.md)
- [00489f8c](../00489/00489f8c.md)
- [00498210](../00498/00498210.md)
- [00498844](../00498/00498844.md)
- [0077bb04](../0077b/0077bb04.md)
- [00851550](../00851/00851550.md)
- [00861508](../00861/00861508.md)
- [008dda58](../008dd/008dda58.md)
- [00acae1c](../00aca/00acae1c.md)
- [00b3bf30](../00b3b/00b3bf30.md)
- [00c57f00](../00c57/00c57f00.md)
- [00c57f20](../00c57/00c57f20.md)
- [00c57f40](../00c57/00c57f40.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c586e0](../00c58/00c586e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 17240 bytes

~~~c

void FUN_008deaac(long param_1,undefined8 param_2)

{
  byte *pbVar1;
  int *piVar2;
  uint uVar3;
  int iVar4;
  int iVar5;
  long lVar6;
  uint uVar7;
  undefined *puVar8;
  int iVar9;
  int iVar10;
  undefined4 uVar11;
  long lVar12;
  long lVar13;
  ulong uVar14;
  undefined8 uVar15;
  float fVar16;
  undefined1 auStack_7c [20];
  long local_68;
  
  lVar6 = tpidr_el0;
  local_68 = *(long *)(lVar6 + 0x28);
  if (((DAT_00ca5038 & 1) == 0) && (iVar9 = __cxa_guard_acquire(&DAT_00ca5038), iVar9 != 0)) {
    DAT_00ca5008 = 0;
    DAT_00ca5000 = &DAT_00ca5008;
    DAT_00ca5028 = 0;
    DAT_00ca5030 = 0;
    DAT_00ca5020 = 0;
    DAT_00ca5010 = 0;
    DAT_00ca5018 = &DAT_00ca5020;
    __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
    __cxa_guard_release(&DAT_00ca5038);
  }
  if (DAT_00ca5030 != 0) {
    FUN_00498210();
  }
  pbVar1 = (byte *)((long)&fde_table_entry_00332060.initial_loc + param_1);
  piVar2 = (int *)((long)&fde_table_entry_00333cc8.data_loc + param_1);
  if (DAT_00ca4a78 == 0) {
    lVar12 = 0;
  }
  else {
    lVar12 = __dynamic_cast(DAT_00ca4a78,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65f28,
                            &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c85168,0);
  }
  iVar9 = FUN_0046ca04(param_1);
  lVar13 = FUN_00489f8c(*(undefined8 *)(lVar12 + 0xf8),0xb);
  iVar9 = iVar9 - *(int *)(lVar13 + 8);
  if (*(char *)(lVar12 + 0x2f0) == '\0') {
LAB_008deb88:
    *(undefined1 *)(lVar12 + 0x2f0) = 0;
    FUN_00467ba0(param_2,0x58,0xb8,0xcc,0xff);
    uVar15 = *(undefined8 *)(lVar12 + 0x128);
                    /* try { // try from 008debac to 009debb7 has its CatchHandler @ 008df020 */
    iVar10 = FUN_0046ca04(param_1);
    FUN_00851550();
    uVar11 = FUN_0046cac4();
                    /* try { // try from 008debcc to 009debe7 has its CatchHandler @ 008df028 */
    FUN_00469c44(param_2,uVar15,0xffffffd8,0,iVar10 + 0x50,uVar11,0x4c);
                    /* try { // try from 008debe8 to 009deeb3 has its CatchHandler @ 008de918 */
    FUN_00467ba0(param_2,0x6c,200,0xce,0xff);
    fVar16 = (float)FUN_0046d9ec((float)*(int *)((long)&fde_table_entry_00333f98.data_loc + param_1)
                                );
    FUN_00468c1c(param_2,(int)(fVar16 * 115.0) + 0x8c);
    uVar15 = *(undefined8 *)(lVar12 + 0x118);
    uVar11 = FUN_0046ca04(param_1);
    FUN_00469c44(param_2,uVar15,0,0,uVar11,0x330,0);
    FUN_00468c1c(param_2,0xff);
    FUN_00467ba0(param_2,0xff,0xff,0xff,0xff);
    FUN_008dda58(param_1 + 0x2158);
    FUN_00468ca0(param_2,0);
    FUN_00861508(param_1,*(undefined8 *)(lVar12 + 200),0,0);
    uVar15 = *(undefined8 *)(lVar12 + 200);
    uVar11 = FUN_0046ca04(param_1);
    FUN_00469c44(param_2,uVar15,0,0,uVar11,0x37,0);
    FUN_00467ba0(param_2,0xff,0xff,0xff,0xff);
    FUN_00468c1c(param_2,0x72);
    if (0 < **(int **)(param_1 + 0x21d8)) {
      uVar15 = *(undefined8 *)(lVar12 + 0xa8);
      lVar13 = FUN_00851550();
      fVar16 = (float)FUN_0046d9b4((float)(*(int *)((long)&fde_table_entry_00333f98.initial_loc +
                                                   lVar13) * 0x1e));
      FUN_00468fc8(param_2,uVar15,(int)(fVar16 * 10.0 + 24.0),0xff,8);
    }
    FUN_00468ca0(param_2,1);
    iVar10 = **(int **)(param_1 + 0x21d8);
    lVar13 = FUN_00851550();
    if (iVar10 < *(int *)((long)&fde_table_entry_00335f78.initial_loc + lVar13) + -1) {
      uVar15 = *(undefined8 *)(lVar12 + 0xa8);
      iVar10 = FUN_0046ca04(param_1);
      lVar13 = FUN_00851550();
      fVar16 = (float)FUN_0046d9b4((float)(*(int *)((long)&fde_table_entry_00333f98.initial_loc +
                                                   lVar13) * 0x1e));
      FUN_00468fc8(param_2,uVar15,(int)((float)(iVar10 + -0x56) + fVar16 * -10.0),0xff,8);
    }
    FUN_00468ca0(param_2,0);
    FUN_00468c1c(param_2,0xff);
    iVar10 = *(int *)((long)&fde_table_entry_00334170.data_loc + param_1);
    if (iVar10 < 0x129) {
      FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0x1f8),8 - iVar10,3,1);
    }
    if (((((((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1) & 1) == 0) &&
           ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) & 1) == 0)) &&
          ((*(byte *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 1) & 1) == 0)) &&
         (((*(byte *)((long)&fde_table_entry_00332a28.initial_loc + param_1 + 1) & 1) == 0 &&
          ((*(byte *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) & 1) == 0)))) &&
        ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 2) & 1) == 0)) &&
       (((*pbVar1 & 1) == 0 &&
        (*(char *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 2) != '\0')))) {
      uVar3 = *(uint *)((long)&fde_table_entry_00333f98.initial_loc + param_1);
      uVar7 = -uVar3;
      uVar3 = uVar3 & 3;
      if (-1 < (int)uVar7) {
        uVar3 = -(uVar7 & 3);
      }
      FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),3,0x21c,0x60,0x60,
                   ((uint)(int)(char)((char)uVar3 + (char)((uVar3 & 0x80) >> 7)) >> 1) + 0xc & 0xff)
      ;
    }
    FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0xf8),iVar9,0,0xb);
                    /* try { // try from 008deeb4 to 009deebf has its CatchHandler @ 008deff4 */
    FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0xf8),iVar9 + -100,0x11,10);
    uVar15 = *(undefined8 *)(lVar12 + 0xf8);
                    /* try { // try from 008deec4 to 009deee3 has its CatchHandler @ 008defe4 */
    iVar10 = FUN_0046ca04(param_1);
    uVar11 = FUN_00b3bf30(param_1 + 0xc570);
                    /* try { // try from 008deee4 to 009df07b has its CatchHandler @ 008de918 */
    FUN_0046af4c(auStack_7c,(float)(iVar10 + -6),0x40c00000,0xbf800000,param_2,uVar15,0,uVar11,0,0,2
                 ,0);
    FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),iVar9 + -0x25,8,0x3e,0x24,0x17);
  }
  else {
    if (((DAT_00ca5038 & 1) == 0) && (iVar10 = __cxa_guard_acquire(&DAT_00ca5038), iVar10 != 0)) {
      DAT_00ca5008 = 0;
      DAT_00ca5000 = &DAT_00ca5008;
      DAT_00ca5028 = 0;
      DAT_00ca5030 = 0;
      DAT_00ca5020 = 0;
      DAT_00ca5010 = 0;
      DAT_00ca5018 = &DAT_00ca5020;
      __cxa_atexit(FUN_0047edf4,&DAT_00ca5000,&PTR_LOOP_00c63060);
      __cxa_guard_release(&DAT_00ca5038);
    }
    if ((DAT_00ca5030 == 0) || (uVar14 = FUN_00498844(), (uVar14 & 1) != 0)) goto LAB_008deb88;
  }
  FUN_00acae1c((long)&fde_table_entry_00337d90.initial_loc + param_1,*(undefined8 *)(lVar12 + 0x1a8)
               ,0);
  if ((((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1) & 1) != 0) ||
      ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) & 1) != 0)) ||
     (*(char *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) != '\0')) {
    FUN_00861508(param_1,*(undefined8 *)(lVar12 + 200),0,0);
    uVar15 = *(undefined8 *)(lVar12 + 200);
    uVar11 = FUN_0046ca04(param_1);
    FUN_00469c44(param_2,uVar15,0,0,uVar11,0x37,0);
    iVar10 = *(int *)((long)&fde_table_entry_00334170.data_loc + param_1);
    if (iVar10 < 0x129) {
      FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0x1f8),8 - iVar10,3,1);
    }
  }
  FUN_00468ca0(param_2,2);
  uVar15 = *(undefined8 *)(lVar12 + 200);
  uVar11 = FUN_0046ca04(param_1);
                    /* catch() { ... } // from try @ 008deec4 with catch @ 008defe4 */
                    /* catch() { ... } // from try @ 008deeb4 with catch @ 008deff4 */
  FUN_00469c44(param_2,uVar15,0,0x249,uVar11,0x37,0);
                    /* catch() { ... } // from try @ 008de9f0 with catch @ 008deffc */
  FUN_00468ca0(param_2,0);
  puVar8 = PTR_DAT_00c9b578;
                    /* catch() { ... } // from try @ 008debac with catch @ 008df020 */
  iVar4 = *(int *)(PTR_DAT_00c9b578 +
                  (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1) * 4);
                    /* catch() { ... } // from try @ 008debcc with catch @ 008df028 */
  iVar10 = iVar4;
  if (iVar4 < 0) {
    iVar10 = iVar4 + 1;
  }
  FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),*piVar2 - (iVar10 >> 1),
               *(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar10 >> 1),
               *(int *)((long)&fde_table_entry_00333cd0.data_loc + param_1) + iVar4,
               *(int *)((long)&fde_table_entry_00333cd8.initial_loc + param_1) + iVar4,9);
  iVar5 = *(int *)(puVar8 + (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1) *
                            4);
  iVar10 = iVar5 + 0x54;
  iVar4 = iVar5 + 0x3c;
  if (iVar5 < 0) {
    iVar5 = iVar5 + 1;
  }
                    /* try { // try from 008df07c to 009df0c3 has its CatchHandler @ 008df07c
                       catch() { ... } // from try @ 008df07c with catch @ 008df07c
                       catch() { ... } // from try @ 008df0dc with catch @ 008df07c */
  FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),(*piVar2 - (iVar5 >> 1)) + 4,
               (*(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar5 >> 1)) +
               0x11,iVar10,iVar4,3);
  if (((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1) & 1) == 0) &&
     ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) & 1) == 0)) {
    if (((((*(byte *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 1) & 1) == 0) &&
         (((*(byte *)((long)&fde_table_entry_00332a28.initial_loc + param_1 + 1) & 1) == 0 &&
          ((*(byte *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) & 1) == 0)))) &&
        ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 2) & 1) == 0)) &&
       (((*pbVar1 & 1) == 0 &&
        (*(char *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 2) != '\0')))) {
      uVar3 = *(uint *)((long)&fde_table_entry_00333f98.initial_loc + param_1);
      uVar7 = -uVar3;
      uVar3 = uVar3 & 3;
      if (-1 < (int)uVar7) {
        uVar3 = -(uVar7 & 3);
      }
      FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),3,0x21c,0x60,0x60,
                   ((uint)(int)(char)((char)uVar3 + (char)((uVar3 & 0x80) >> 7)) >> 1) + 0xc & 0xff)
      ;
      if (*(char *)((long)&fde_table_entry_00332a20.data_loc + param_1) == '\0' &&
          *(char *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) == '\0') {
LAB_008df0cc:
        if (*(char *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) == '\0')
        goto LAB_008df178;
      }
    }
    else {
                    /* try { // try from 008df0c4 to 009df0db has its CatchHandler @ 008df110 */
      if (*(char *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) == '\0')
      goto LAB_008df0cc;
    }
  }
                    /* try { // try from 008df0dc to 009df13f has its CatchHandler @ 008df07c */
  FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0xf8),iVar9,0,0xb);
  FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0xf8),iVar9 + -100,0x11,10);
  uVar15 = *(undefined8 *)(lVar12 + 0xf8);
  iVar10 = FUN_0046ca04(param_1);
                    /* catch() { ... } // from try @ 008df0c4 with catch @ 008df110 */
  uVar11 = FUN_00b3bf30(param_1 + 0xc570);
                    /* try { // try from 008df140 to 009e348b has its CatchHandler @ 008df140
                       catch() { ... } // from try @ 008df140 with catch @ 008df140
                       catch() { ... } // from try @ 008e34b8 with catch @ 008df140
                       catch() { ... } // from try @ 008e53d4 with catch @ 008df140
                       catch() { ... } // from try @ 008e6074 with catch @ 008df140
                       catch() { ... } // from try @ 008e6110 with catch @ 008df140
                       catch() { ... } // from try @ 008e6218 with catch @ 008df140
                       catch() { ... } // from try @ 008e62b4 with catch @ 008df140
                       catch() { ... } // from try @ 008e78d0 with catch @ 008df140
                       catch() { ... } // from try @ 008e7b28 with catch @ 008df140
                       catch() { ... } // from try @ 008e7c3c with catch @ 008df140
                       catch() { ... } // from try @ 008e7f54 with catch @ 008df140
                       catch() { ... } // from try @ 008e94b0 with catch @ 008df140
                       catch() { ... } // from try @ 008eadb0 with catch @ 008df140
                       catch() { ... } // from try @ 008eae20 with catch @ 008df140
                       catch() { ... } // from try @ 008eae8c with catch @ 008df140
                       catch() { ... } // from try @ 008eaef8 with catch @ 008df140
                       catch() { ... } // from try @ 008eb0a4 with catch @ 008df140
                       catch() { ... } // from try @ 008eb118 with catch @ 008df140
                       catch() { ... } // from try @ 008eb180 with catch @ 008df140
                       catch() { ... } // from try @ 008eb1e8 with catch @ 008df140
                       catch() { ... } // from try @ 008eb2a8 with catch @ 008df140
                       catch() { ... } // from try @ 008eb314 with catch @ 008df140
                       catch() { ... } // from try @ 008eb37c with catch @ 008df140
                       catch() { ... } // from try @ 008eb3e4 with catch @ 008df140
                       catch() { ... } // from try @ 008eb8dc with catch @ 008df140
                       catch() { ... } // from try @ 008eb94c with catch @ 008df140
                       catch() { ... } // from try @ 008eb9b8 with catch @ 008df140
                       catch() { ... } // from try @ 008eba24 with catch @ 008df140
                       catch() { ... } // from try @ 008ebc34 with catch @ 008df140
                       catch() { ... } // from try @ 008ebcd4 with catch @ 008df140
                       catch() { ... } // from try @ 008ec030 with catch @ 008df140
                       catch() { ... } // from try @ 008eccd8 with catch @ 008df140
                       catch() { ... } // from try @ 008ece58 with catch @ 008df140
                       catch() { ... } // from try @ 008ed218 with catch @ 008df140
                       catch() { ... } // from try @ 008ede1c with catch @ 008df140
                       catch() { ... } // from try @ 008ee208 with catch @ 008df140
                       catch() { ... } // from try @ 008ee2d4 with catch @ 008df140
                       catch() { ... } // from try @ 008ee2f8 with catch @ 008df140
                       catch() { ... } // from try @ 008ef098 with catch @ 008df140 */
  FUN_0046af4c(auStack_7c,(float)(iVar10 + -6),0x40c00000,0xbf800000,param_2,uVar15,0,uVar11,0,0,2,0
              );
  FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),iVar9 + -0x25,8,0x3e,0x24,0x17);
LAB_008df178:
  FUN_00468ca0(param_2,2);
  FUN_00468fc8(param_2,*(undefined8 *)(lVar12 + 0xf8),iVar9,0x249,0xb);
  FUN_00468ca0(param_2,0);
  FUN_0077bb04(param_1,param_2,*(undefined8 *)(lVar12 + 0xa8),iVar9,1,0);
  uVar15 = *(undefined8 *)(lVar12 + 0xf8);
  iVar9 = FUN_0046ca04(param_1);
  uVar11 = FUN_00b3bf30(param_1 + 0xc400);
  FUN_0046af4c(auStack_7c,(float)(iVar9 + -6),0x44140000,0xbf800000,param_2,uVar15,0,uVar11,0,0,2,0)
  ;
  iVar10 = *(int *)(puVar8 + (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1) *
                             4);
  iVar9 = iVar10;
  if (iVar10 < 0) {
    iVar9 = iVar10 + 1;
  }
  FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),*piVar2 - (iVar9 >> 1),
               *(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar9 >> 1),
               *(int *)((long)&fde_table_entry_00333cd0.data_loc + param_1) + iVar10,
               *(int *)((long)&fde_table_entry_00333cd8.initial_loc + param_1) + iVar10,9);
  iVar4 = *(int *)(puVar8 + (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1) *
                            4);
  iVar9 = iVar4 + 0x54;
  iVar10 = iVar4 + 0x3c;
  if (iVar4 < 0) {
    iVar4 = iVar4 + 1;
  }
  FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),(*piVar2 - (iVar4 >> 1)) + 4,
               (*(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar4 >> 1)) +
               0x11,iVar9,iVar10,3);
  if (((((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1) & 1) == 0) &&
       ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) & 1) == 0)) &&
      ((*(byte *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 1) & 1) == 0)) &&
     ((((*(byte *)((long)&fde_table_entry_00332a28.initial_loc + param_1 + 1) & 1) == 0 &&
       ((*(byte *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) & 1) == 0)) &&
      (((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 2) & 1) == 0 &&
       (((*pbVar1 & 1) == 0 &&
        (*(char *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 2) != '\0')))))))) {
    uVar3 = *(uint *)((long)&fde_table_entry_00333f98.initial_loc + param_1);
    uVar7 = -uVar3;
    uVar3 = uVar3 & 3;
    if (-1 < (int)uVar7) {
      uVar3 = -(uVar7 & 3);
    }
    FUN_00469c44(param_2,*(undefined8 *)(lVar12 + 0xa8),3,0x21c,0x60,0x60,
                 ((uint)(int)(char)((char)uVar3 + (char)((uVar3 & 0x80) >> 7)) >> 1) + 0xc & 0xff);
  }
  if (*(long *)(lVar6 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008deaac"></a> `008deaac` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-008deab0"></a> `008deab0` | `e8 13 00 fd` | str d8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008deab4"></a> `008deab4` | `fd fb 02 a9` | stp x29,x30,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-008deab8"></a> `008deab8` | `fb 1f 00 f9` | str x27,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-008deabc"></a> `008deabc` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008deac0"></a> `008deac0` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008deac4"></a> `008deac4` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008deac8"></a> `008deac8` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008deacc"></a> `008deacc` | `fd a3 00 91` | add x29,sp,#0x28 | `FALL_THROUGH`
<a id="insn-008dead0"></a> `008dead0` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-008dead4"></a> `008dead4` | `37 1e 00 f0` | adrp x23,0xca5000 | `FALL_THROUGH`
<a id="insn-008dead8"></a> `008dead8` | `f7 e2 00 91` | add x23,x23,#0x38 | `FALL_THROUGH`
<a id="insn-008deadc"></a> `008deadc` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-008deae0"></a> `008deae0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-008deae4"></a> `008deae4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-008deae8"></a> `008deae8` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-008deaec"></a> `008deaec` | `e8 fe df 08` | ldarb w8,[x23] | `FALL_THROUGH`
<a id="insn-008deaf0"></a> `008deaf0` | `48 46 00 36` | tbz w8,#0x0,0x008df3b8 | `CONDITIONAL_JUMP`
<a id="insn-008deaf4"></a> `008deaf4` | `38 1e 00 f0` | adrp x24,0xca5000 | `FALL_THROUGH`
<a id="insn-008deaf8"></a> `008deaf8` | `00 1b 40 f9` | ldr x0,[x24, #0x30] | `FALL_THROUGH`
<a id="insn-008deafc"></a> `008deafc` | `40 00 00 b4` | cbz x0,0x008deb04 | `CONDITIONAL_JUMP`
<a id="insn-008deb00"></a> `008deb00` | `c4 e5 ee 97` | bl 0x00498210 | `UNCONDITIONAL_CALL`
<a id="insn-008deb04"></a> `008deb04` | `28 1e 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-008deb08"></a> `008deb08` | `a9 ca 4c 91` | add x9,x21,#0x332, LSL #12 | `FALL_THROUGH`
<a id="insn-008deb0c"></a> `008deb0c` | `00 3d 45 f9` | ldr x0,[x8, #0xa78] | `FALL_THROUGH`
<a id="insn-008deb10"></a> `008deb10` | `a8 ce 4c 91` | add x8,x21,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-008deb14"></a> `008deb14` | `3b 81 01 91` | add x27,x9,#0x60 | `FALL_THROUGH`
<a id="insn-008deb18"></a> `008deb18` | `1a 31 33 91` | add x26,x8,#0xccc | `FALL_THROUGH`
<a id="insn-008deb1c"></a> `008deb1c` | `20 01 00 b4` | cbz x0,0x008deb40 | `CONDITIONAL_JUMP`
<a id="insn-008deb20"></a> `008deb20` | `21 1c 00 f0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-008deb24"></a> `008deb24` | `21 a0 3c 91` | add x1,x1,#0xf28 | `FALL_THROUGH`
<a id="insn-008deb28"></a> `008deb28` | `22 1d 00 f0` | adrp x2,0xc85000 | `FALL_THROUGH`
<a id="insn-008deb2c"></a> `008deb2c` | `42 a0 05 91` | add x2,x2,#0x168 | `FALL_THROUGH`
<a id="insn-008deb30"></a> `008deb30` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-008deb34"></a> `008deb34` | `eb e6 0d 94` | bl 0x00c586e0 | `UNCONDITIONAL_CALL`
<a id="insn-008deb38"></a> `008deb38` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-008deb3c"></a> `008deb3c` | `02 00 00 14` | b 0x008deb44 | `UNCONDITIONAL_JUMP`
<a id="insn-008deb40"></a> `008deb40` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-008deb44"></a> `008deb44` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008deb48"></a> `008deb48` | `af 37 ee 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-008deb4c"></a> `008deb4c` | `88 7e 40 f9` | ldr x8,[x20, #0xf8] | `FALL_THROUGH`
<a id="insn-008deb50"></a> `008deb50` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-008deb54"></a> `008deb54` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-008deb58"></a> `008deb58` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-008deb5c"></a> `008deb5c` | `0c ad ee 97` | bl 0x00489f8c | `UNCONDITIONAL_CALL`
<a id="insn-008deb60"></a> `008deb60` | `09 08 40 b9` | ldr w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-008deb64"></a> `008deb64` | `88 c2 4b 39` | ldrb w8,[x20, #0x2f0] | `FALL_THROUGH`
<a id="insn-008deb68"></a> `008deb68` | `d6 02 09 4b` | sub w22,w22,w9 | `FALL_THROUGH`
<a id="insn-008deb6c"></a> `008deb6c` | `e8 00 00 34` | cbz w8,0x008deb88 | `CONDITIONAL_JUMP`
<a id="insn-008deb70"></a> `008deb70` | `e8 fe df 08` | ldarb w8,[x23] | `FALL_THROUGH`
<a id="insn-008deb74"></a> `008deb74` | `08 45 00 36` | tbz w8,#0x0,0x008df414 | `CONDITIONAL_JUMP`
<a id="insn-008deb78"></a> `008deb78` | `00 1b 40 f9` | ldr x0,[x24, #0x30] | `FALL_THROUGH`
<a id="insn-008deb7c"></a> `008deb7c` | `60 00 00 b4` | cbz x0,0x008deb88 | `CONDITIONAL_JUMP`
<a id="insn-008deb80"></a> `008deb80` | `31 e7 ee 97` | bl 0x00498844 | `UNCONDITIONAL_CALL`
<a id="insn-008deb84"></a> `008deb84` | `60 1d 00 36` | tbz w0,#0x0,0x008def30 | `CONDITIONAL_JUMP`
<a id="insn-008deb88"></a> `008deb88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008deb8c"></a> `008deb8c` | `01 0b 80 52` | mov w1,#0x58 | `FALL_THROUGH`
<a id="insn-008deb90"></a> `008deb90` | `02 17 80 52` | mov w2,#0xb8 | `FALL_THROUGH`
<a id="insn-008deb94"></a> `008deb94` | `83 19 80 52` | mov w3,#0xcc | `FALL_THROUGH`
<a id="insn-008deb98"></a> `008deb98` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-008deb9c"></a> `008deb9c` | `9f c2 0b 39` | strb wzr,[x20, #0x2f0] | `FALL_THROUGH`
<a id="insn-008deba0"></a> `008deba0` | `00 24 ee 97` | bl 0x00467ba0 | `UNCONDITIONAL_CALL`
<a id="insn-008deba4"></a> `008deba4` | `97 96 40 f9` | ldr x23,[x20, #0x128] | `FALL_THROUGH`
<a id="insn-008deba8"></a> `008deba8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008debac"></a> `008debac` | `96 37 ee 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-008debb0"></a> `008debb0` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-008debb4"></a> `008debb4` | `67 ca fd 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008debb8"></a> `008debb8` | `c3 37 ee 97` | bl 0x0046cac4 | `UNCONDITIONAL_CALL`
<a id="insn-008debbc"></a> `008debbc` | `e5 03 00 2a` | mov w5,w0 | `FALL_THROUGH`
<a id="insn-008debc0"></a> `008debc0` | `04 43 01 11` | add w4,w24,#0x50 | `FALL_THROUGH`
<a id="insn-008debc4"></a> `008debc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008debc8"></a> `008debc8` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-008debcc"></a> `008debcc` | `e2 04 80 12` | mov w2,#0xffffffd8 | `FALL_THROUGH`
<a id="insn-008debd0"></a> `008debd0` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-008debd4"></a> `008debd4` | `86 09 80 52` | mov w6,#0x4c | `FALL_THROUGH`
<a id="insn-008debd8"></a> `008debd8` | `1b 2c ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008debdc"></a> `008debdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008debe0"></a> `008debe0` | `81 0d 80 52` | mov w1,#0x6c | `FALL_THROUGH`
<a id="insn-008debe4"></a> `008debe4` | `02 19 80 52` | mov w2,#0xc8 | `FALL_THROUGH`
<a id="insn-008debe8"></a> `008debe8` | `c3 19 80 52` | mov w3,#0xce | `FALL_THROUGH`
<a id="insn-008debec"></a> `008debec` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-008debf0"></a> `008debf0` | `ec 23 ee 97` | bl 0x00467ba0 | `UNCONDITIONAL_CALL`
<a id="insn-008debf4"></a> `008debf4` | `40 d3 42 bd` | ldr s0,[x26, #0x2d0] | `FALL_THROUGH`
<a id="insn-008debf8"></a> `008debf8` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-008debfc"></a> `008debfc` | `7c 3b ee 97` | bl 0x0046d9ec | `UNCONDITIONAL_CALL`
<a id="insn-008dec00"></a> `008dec00` | `c8 5c a8 52` | mov w8,#0x42e60000 | `FALL_THROUGH`
<a id="insn-008dec04"></a> `008dec04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dec08"></a> `008dec08` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-008dec0c"></a> `008dec0c` | `00 08 21 1e` | fmul s0,s0,s1 | `FALL_THROUGH`
<a id="insn-008dec10"></a> `008dec10` | `08 00 38 1e` | fcvtzs w8,s0 | `FALL_THROUGH`
<a id="insn-008dec14"></a> `008dec14` | `01 31 02 11` | add w1,w8,#0x8c | `FALL_THROUGH`
<a id="insn-008dec18"></a> `008dec18` | `01 28 ee 97` | bl 0x00468c1c | `UNCONDITIONAL_CALL`
<a id="insn-008dec1c"></a> `008dec1c` | `97 8e 40 f9` | ldr x23,[x20, #0x118] | `FALL_THROUGH`
<a id="insn-008dec20"></a> `008dec20` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008dec24"></a> `008dec24` | `78 37 ee 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-008dec28"></a> `008dec28` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-008dec2c"></a> `008dec2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dec30"></a> `008dec30` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-008dec34"></a> `008dec34` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-008dec38"></a> `008dec38` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-008dec3c"></a> `008dec3c` | `05 66 80 52` | mov w5,#0x330 | `FALL_THROUGH`
<a id="insn-008dec40"></a> `008dec40` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-008dec44"></a> `008dec44` | `00 2c ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008dec48"></a> `008dec48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dec4c"></a> `008dec4c` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-008dec50"></a> `008dec50` | `f3 27 ee 97` | bl 0x00468c1c | `UNCONDITIONAL_CALL`
<a id="insn-008dec54"></a> `008dec54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dec58"></a> `008dec58` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-008dec5c"></a> `008dec5c` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-008dec60"></a> `008dec60` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-008dec64"></a> `008dec64` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-008dec68"></a> `008dec68` | `ce 23 ee 97` | bl 0x00467ba0 | `UNCONDITIONAL_CALL`
<a id="insn-008dec6c"></a> `008dec6c` | `08 2b 84 52` | mov w8,#0x2158 | `FALL_THROUGH`
<a id="insn-008dec70"></a> `008dec70` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-008dec74"></a> `008dec74` | `79 fb ff 97` | bl 0x008dda58 | `UNCONDITIONAL_CALL`
<a id="insn-008dec78"></a> `008dec78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dec7c"></a> `008dec7c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-008dec80"></a> `008dec80` | `08 28 ee 97` | bl 0x00468ca0 | `UNCONDITIONAL_CALL`
<a id="insn-008dec84"></a> `008dec84` | `81 66 40 f9` | ldr x1,[x20, #0xc8] | `FALL_THROUGH`
<a id="insn-008dec88"></a> `008dec88` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008dec8c"></a> `008dec8c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-008dec90"></a> `008dec90` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-008dec94"></a> `008dec94` | `1d 0a fe 97` | bl 0x00861508 | `UNCONDITIONAL_CALL`
<a id="insn-008dec98"></a> `008dec98` | `97 66 40 f9` | ldr x23,[x20, #0xc8] | `FALL_THROUGH`
<a id="insn-008dec9c"></a> `008dec9c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008deca0"></a> `008deca0` | `59 37 ee 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-008deca4"></a> `008deca4` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-008deca8"></a> `008deca8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008decac"></a> `008decac` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-008decb0"></a> `008decb0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-008decb4"></a> `008decb4` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-008decb8"></a> `008decb8` | `e5 06 80 52` | mov w5,#0x37 | `FALL_THROUGH`
<a id="insn-008decbc"></a> `008decbc` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-008decc0"></a> `008decc0` | `e1 2b ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008decc4"></a> `008decc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008decc8"></a> `008decc8` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-008deccc"></a> `008deccc` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-008decd0"></a> `008decd0` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-008decd4"></a> `008decd4` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-008decd8"></a> `008decd8` | `b2 23 ee 97` | bl 0x00467ba0 | `UNCONDITIONAL_CALL`
<a id="insn-008decdc"></a> `008decdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dece0"></a> `008dece0` | `41 0e 80 52` | mov w1,#0x72 | `FALL_THROUGH`
<a id="insn-008dece4"></a> `008dece4` | `ce 27 ee 97` | bl 0x00468c1c | `UNCONDITIONAL_CALL`
<a id="insn-008dece8"></a> `008dece8` | `a8 ee 50 f9` | ldr x8,[x21, #0x21d8] | `FALL_THROUGH`
<a id="insn-008decec"></a> `008decec` | `08 01 40 b9` | ldr w8,[x8] | `FALL_THROUGH`
<a id="insn-008decf0"></a> `008decf0` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-008decf4"></a> `008decf4` | `6b 02 00 54` | b.lt 0x008ded40 | `CONDITIONAL_JUMP`
<a id="insn-008decf8"></a> `008decf8` | `97 56 40 f9` | ldr x23,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-008decfc"></a> `008decfc` | `15 ca fd 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008ded00"></a> `008ded00` | `08 f3 87 52` | mov w8,#0x3f98 | `FALL_THROUGH`
<a id="insn-008ded04"></a> `008ded04` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-008ded08"></a> `008ded08` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008ded0c"></a> `008ded0c` | `09 69 1b 53` | lsl w9,w8,#0x5 | `FALL_THROUGH`
<a id="insn-008ded10"></a> `008ded10` | `28 05 08 4b` | sub w8,w9,w8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-008ded14"></a> `008ded14` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-008ded18"></a> `008ded18` | `27 3b ee 97` | bl 0x0046d9b4 | `UNCONDITIONAL_CALL`
<a id="insn-008ded1c"></a> `008ded1c` | `01 10 27 1e` | fmov s1,0x41c00000 | `FALL_THROUGH`
<a id="insn-008ded20"></a> `008ded20` | `02 90 24 1e` | fmov s2,0x41200000 | `FALL_THROUGH`
<a id="insn-008ded24"></a> `008ded24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008ded28"></a> `008ded28` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-008ded2c"></a> `008ded2c` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-008ded30"></a> `008ded30` | `04 01 80 52` | mov w4,#0x8 | `FALL_THROUGH`
<a id="insn-008ded34"></a> `008ded34` | `00 04 02 1f` | fmadd s0,s0,s2,s1 | `FALL_THROUGH`
<a id="insn-008ded38"></a> `008ded38` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-008ded3c"></a> `008ded3c` | `a3 28 ee 97` | bl 0x00468fc8 | `UNCONDITIONAL_CALL`
<a id="insn-008ded40"></a> `008ded40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008ded44"></a> `008ded44` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-008ded48"></a> `008ded48` | `d6 27 ee 97` | bl 0x00468ca0 | `UNCONDITIONAL_CALL`
<a id="insn-008ded4c"></a> `008ded4c` | `a8 ee 50 f9` | ldr x8,[x21, #0x21d8] | `FALL_THROUGH`
<a id="insn-008ded50"></a> `008ded50` | `17 01 40 b9` | ldr w23,[x8] | `FALL_THROUGH`
<a id="insn-008ded54"></a> `008ded54` | `ff c9 fd 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008ded58"></a> `008ded58` | `08 ef 8b 52` | mov w8,#0x5f78 | `FALL_THROUGH`
<a id="insn-008ded5c"></a> `008ded5c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-008ded60"></a> `008ded60` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008ded64"></a> `008ded64` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-008ded68"></a> `008ded68` | `ff 02 08 6b` | cmp w23,w8 | `FALL_THROUGH`
<a id="insn-008ded6c"></a> `008ded6c` | `ca 02 00 54` | b.ge 0x008dedc4 | `CONDITIONAL_JUMP`
<a id="insn-008ded70"></a> `008ded70` | `97 56 40 f9` | ldr x23,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-008ded74"></a> `008ded74` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008ded78"></a> `008ded78` | `23 37 ee 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-008ded7c"></a> `008ded7c` | `08 58 01 51` | sub w8,w0,#0x56 | `FALL_THROUGH`
<a id="insn-008ded80"></a> `008ded80` | `08 01 22 1e` | scvtf s8,w8 | `FALL_THROUGH`
<a id="insn-008ded84"></a> `008ded84` | `f3 c9 fd 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-008ded88"></a> `008ded88` | `08 f3 87 52` | mov w8,#0x3f98 | `FALL_THROUGH`
<a id="insn-008ded8c"></a> `008ded8c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-008ded90"></a> `008ded90` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008ded94"></a> `008ded94` | `09 69 1b 53` | lsl w9,w8,#0x5 | `FALL_THROUGH`
<a id="insn-008ded98"></a> `008ded98` | `28 05 08 4b` | sub w8,w9,w8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-008ded9c"></a> `008ded9c` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-008deda0"></a> `008deda0` | `05 3b ee 97` | bl 0x0046d9b4 | `UNCONDITIONAL_CALL`
<a id="insn-008deda4"></a> `008deda4` | `01 90 34 1e` | fmov s1,0xc1200000 | `FALL_THROUGH`
<a id="insn-008deda8"></a> `008deda8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dedac"></a> `008dedac` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-008dedb0"></a> `008dedb0` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-008dedb4"></a> `008dedb4` | `04 01 80 52` | mov w4,#0x8 | `FALL_THROUGH`
<a id="insn-008dedb8"></a> `008dedb8` | `00 20 01 1f` | fmadd s0,s0,s1,s8 | `FALL_THROUGH`
<a id="insn-008dedbc"></a> `008dedbc` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-008dedc0"></a> `008dedc0` | `82 28 ee 97` | bl 0x00468fc8 | `UNCONDITIONAL_CALL`
<a id="insn-008dedc4"></a> `008dedc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dedc8"></a> `008dedc8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-008dedcc"></a> `008dedcc` | `b5 27 ee 97` | bl 0x00468ca0 | `UNCONDITIONAL_CALL`
<a id="insn-008dedd0"></a> `008dedd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dedd4"></a> `008dedd4` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-008dedd8"></a> `008dedd8` | `91 27 ee 97` | bl 0x00468c1c | `UNCONDITIONAL_CALL`
<a id="insn-008deddc"></a> `008deddc` | `48 ab 44 b9` | ldr w8,[x26, #0x4a8] | `FALL_THROUGH`
<a id="insn-008dede0"></a> `008dede0` | `1f a1 04 71` | cmp w8,#0x128 | `FALL_THROUGH`
<a id="insn-008dede4"></a> `008dede4` | `0c 01 00 54` | b.gt 0x008dee04 | `CONDITIONAL_JUMP`
<a id="insn-008dede8"></a> `008dede8` | `81 fe 40 f9` | ldr x1,[x20, #0x1f8] | `FALL_THROUGH`
<a id="insn-008dedec"></a> `008dedec` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-008dedf0"></a> `008dedf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dedf4"></a> `008dedf4` | `22 01 08 4b` | sub w2,w9,w8 | `FALL_THROUGH`
<a id="insn-008dedf8"></a> `008dedf8` | `63 00 80 52` | mov w3,#0x3 | `FALL_THROUGH`
<a id="insn-008dedfc"></a> `008dedfc` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-008dee00"></a> `008dee00` | `72 28 ee 97` | bl 0x00468fc8 | `UNCONDITIONAL_CALL`
<a id="insn-008dee04"></a> `008dee04` | `68 13 67 39` | ldrb w8,[x27, #0x9c4] | `FALL_THROUGH`
<a id="insn-008dee08"></a> `008dee08` | `28 04 00 37` | tbnz w8,#0x0,0x008dee8c | `CONDITIONAL_JUMP`
<a id="insn-008dee0c"></a> `008dee0c` | `68 17 67 39` | ldrb w8,[x27, #0x9c5] | `FALL_THROUGH`
<a id="insn-008dee10"></a> `008dee10` | `e8 03 00 37` | tbnz w8,#0x0,0x008dee8c | `CONDITIONAL_JUMP`
<a id="insn-008dee14"></a> `008dee14` | `68 37 67 39` | ldrb w8,[x27, #0x9cd] | `FALL_THROUGH`
<a id="insn-008dee18"></a> `008dee18` | `a8 03 00 37` | tbnz w8,#0x0,0x008dee8c | `CONDITIONAL_JUMP`
<a id="insn-008dee1c"></a> `008dee1c` | `68 27 67 39` | ldrb w8,[x27, #0x9c9] | `FALL_THROUGH`
<a id="insn-008dee20"></a> `008dee20` | `68 03 00 37` | tbnz w8,#0x0,0x008dee8c | `CONDITIONAL_JUMP`
<a id="insn-008dee24"></a> `008dee24` | `68 47 67 39` | ldrb w8,[x27, #0x9d1] | `FALL_THROUGH`
<a id="insn-008dee28"></a> `008dee28` | `28 03 00 37` | tbnz w8,#0x0,0x008dee8c | `CONDITIONAL_JUMP`
<a id="insn-008dee2c"></a> `008dee2c` | `68 1b 67 39` | ldrb w8,[x27, #0x9c6] | `FALL_THROUGH`
<a id="insn-008dee30"></a> `008dee30` | `e8 02 00 37` | tbnz w8,#0x0,0x008dee8c | `CONDITIONAL_JUMP`
<a id="insn-008dee34"></a> `008dee34` | `68 03 40 39` | ldrb w8,[x27] | `FALL_THROUGH`
<a id="insn-008dee38"></a> `008dee38` | `a8 02 00 37` | tbnz w8,#0x0,0x008dee8c | `CONDITIONAL_JUMP`
<a id="insn-008dee3c"></a> `008dee3c` | `68 3b 67 39` | ldrb w8,[x27, #0x9ce] | `FALL_THROUGH`
<a id="insn-008dee40"></a> `008dee40` | `68 02 00 34` | cbz w8,0x008dee8c | `CONDITIONAL_JUMP`
<a id="insn-008dee44"></a> `008dee44` | `48 cf 42 b9` | ldr w8,[x26, #0x2cc] | `FALL_THROUGH`
<a id="insn-008dee48"></a> `008dee48` | `81 56 40 f9` | ldr x1,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-008dee4c"></a> `008dee4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dee50"></a> `008dee50` | `62 00 80 52` | mov w2,#0x3 | `FALL_THROUGH`
<a id="insn-008dee54"></a> `008dee54` | `83 43 80 52` | mov w3,#0x21c | `FALL_THROUGH`
<a id="insn-008dee58"></a> `008dee58` | `04 0c 80 52` | mov w4,#0x60 | `FALL_THROUGH`
<a id="insn-008dee5c"></a> `008dee5c` | `e9 03 08 6b` | negs w9,w8 | `FALL_THROUGH`
<a id="insn-008dee60"></a> `008dee60` | `08 05 00 12` | and w8,w8,#0x3 | `FALL_THROUGH`
<a id="insn-008dee64"></a> `008dee64` | `05 0c 80 52` | mov w5,#0x60 | `FALL_THROUGH`
<a id="insn-008dee68"></a> `008dee68` | `29 05 00 12` | and w9,w9,#0x3 | `FALL_THROUGH`
<a id="insn-008dee6c"></a> `008dee6c` | `08 45 89 5a` | csneg w8,w8,w9,mi | `FALL_THROUGH`
<a id="insn-008dee70"></a> `008dee70` | `09 01 19 12` | and w9,w8,#0x80 | `FALL_THROUGH`
<a id="insn-008dee74"></a> `008dee74` | `08 1d 49 0b` | add w8,w8,w9, LSR #0x7 | `FALL_THROUGH`
<a id="insn-008dee78"></a> `008dee78` | `08 1d 00 13` | sxtb w8,w8 | `FALL_THROUGH`
<a id="insn-008dee7c"></a> `008dee7c` | `08 7d 01 53` | lsr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-008dee80"></a> `008dee80` | `08 31 00 11` | add w8,w8,#0xc | `FALL_THROUGH`
<a id="insn-008dee84"></a> `008dee84` | `06 1d 00 12` | and w6,w8,#0xff | `FALL_THROUGH`
<a id="insn-008dee88"></a> `008dee88` | `6f 2b ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008dee8c"></a> `008dee8c` | `81 7e 40 f9` | ldr x1,[x20, #0xf8] | `FALL_THROUGH`
<a id="insn-008dee90"></a> `008dee90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008dee94"></a> `008dee94` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-008dee98"></a> `008dee98` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-008dee9c"></a> `008dee9c` | `64 01 80 52` | mov w4,#0xb | `FALL_THROUGH`
<a id="insn-008deea0"></a> `008deea0` | `4a 28 ee 97` | bl 0x00468fc8 | `UNCONDITIONAL_CALL`
<a id="insn-008deea4"></a> `008deea4` | `81 7e 40 f9` | ldr x1,[x20, #0xf8] | `FALL_THROUGH`
<a id="insn-008deea8"></a> `008deea8` | `c2 92 01 51` | sub w2,w22,#0x64 | `FALL_THROUGH`
<a id="insn-008deeac"></a> `008deeac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008deeb0"></a> `008deeb0` | `23 02 80 52` | mov w3,#0x11 | `FALL_THROUGH`
<a id="insn-008deeb4"></a> `008deeb4` | `44 01 80 52` | mov w4,#0xa | `FALL_THROUGH`
<a id="insn-008deeb8"></a> `008deeb8` | `44 28 ee 97` | bl 0x00468fc8 | `UNCONDITIONAL_CALL`
<a id="insn-008deebc"></a> `008deebc` | `97 7e 40 f9` | ldr x23,[x20, #0xf8] | `FALL_THROUGH`
<a id="insn-008deec0"></a> `008deec0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008deec4"></a> `008deec4` | `d0 36 ee 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-008deec8"></a> `008deec8` | `08 18 00 51` | sub w8,w0,#0x6 | `FALL_THROUGH`
<a id="insn-008deecc"></a> `008deecc` | `08 01 22 1e` | scvtf s8,w8 | `FALL_THROUGH`
<a id="insn-008deed0"></a> `008deed0` | `08 ae 98 52` | mov w8,#0xc570 | `FALL_THROUGH`
<a id="insn-008deed4"></a> `008deed4` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-008deed8"></a> `008deed8` | `16 74 09 94` | bl 0x00b3bf30 | `UNCONDITIONAL_CALL`
<a id="insn-008deedc"></a> `008deedc` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-008deee0"></a> `008deee0` | `01 10 23 1e` | fmov s1,0x40c00000 | `FALL_THROUGH`
<a id="insn-008deee4"></a> `008deee4` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-008deee8"></a> `008deee8` | `02 10 3e 1e` | fmov s2,0xbf800000 | `FALL_THROUGH`
<a id="insn-008deeec"></a> `008deeec` | `e8 13 00 91` | add x8,sp,#0x4 | `FALL_THROUGH`
<a id="insn-008deef0"></a> `008deef0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008deef4"></a> `008deef4` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-008deef8"></a> `008deef8` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-008deefc"></a> `008deefc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-008def00"></a> `008def00` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-008def04"></a> `008def04` | `46 00 80 52` | mov w6,#0x2 | `FALL_THROUGH`
<a id="insn-008def08"></a> `008def08` | `e7 03 1f 2a` | mov w7,wzr | `FALL_THROUGH`
<a id="insn-008def0c"></a> `008def0c` | `10 30 ee 97` | bl 0x0046af4c | `UNCONDITIONAL_CALL`
<a id="insn-008def10"></a> `008def10` | `81 56 40 f9` | ldr x1,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-008def14"></a> `008def14` | `c2 96 00 51` | sub w2,w22,#0x25 | `FALL_THROUGH`
<a id="insn-008def18"></a> `008def18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008def1c"></a> `008def1c` | `03 01 80 52` | mov w3,#0x8 | `FALL_THROUGH`
<a id="insn-008def20"></a> `008def20` | `c4 07 80 52` | mov w4,#0x3e | `FALL_THROUGH`
<a id="insn-008def24"></a> `008def24` | `85 04 80 52` | mov w5,#0x24 | `FALL_THROUGH`
<a id="insn-008def28"></a> `008def28` | `e6 02 80 52` | mov w6,#0x17 | `FALL_THROUGH`
<a id="insn-008def2c"></a> `008def2c` | `46 2b ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008def30"></a> `008def30` | `81 d6 40 f9` | ldr x1,[x20, #0x1a8] | `FALL_THROUGH`
<a id="insn-008def34"></a> `008def34` | `a8 de 4c 91` | add x8,x21,#0x337, LSL #12 | `FALL_THROUGH`
<a id="insn-008def38"></a> `008def38` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-008def3c"></a> `008def3c` | `00 41 36 91` | add x0,x8,#0xd90 | `FALL_THROUGH`
<a id="insn-008def40"></a> `008def40` | `b7 af 07 94` | bl 0x00acae1c | `UNCONDITIONAL_CALL`
<a id="insn-008def44"></a> `008def44` | `68 13 67 39` | ldrb w8,[x27, #0x9c4] | `FALL_THROUGH`
<a id="insn-008def48"></a> `008def48` | `a8 00 00 37` | tbnz w8,#0x0,0x008def5c | `CONDITIONAL_JUMP`
<a id="insn-008def4c"></a> `008def4c` | `68 17 67 39` | ldrb w8,[x27, #0x9c5] | `FALL_THROUGH`
<a id="insn-008def50"></a> `008def50` | `68 00 00 37` | tbnz w8,#0x0,0x008def5c | `CONDITIONAL_JUMP`
<a id="insn-008def54"></a> `008def54` | `68 47 67 39` | ldrb w8,[x27, #0x9d1] | `FALL_THROUGH`
<a id="insn-008def58"></a> `008def58` | `68 03 00 34` | cbz w8,0x008defc4 | `CONDITIONAL_JUMP`
<a id="insn-008def5c"></a> `008def5c` | `81 66 40 f9` | ldr x1,[x20, #0xc8] | `FALL_THROUGH`
<a id="insn-008def60"></a> `008def60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008def64"></a> `008def64` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-008def68"></a> `008def68` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-008def6c"></a> `008def6c` | `67 09 fe 97` | bl 0x00861508 | `UNCONDITIONAL_CALL`
<a id="insn-008def70"></a> `008def70` | `97 66 40 f9` | ldr x23,[x20, #0xc8] | `FALL_THROUGH`
<a id="insn-008def74"></a> `008def74` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008def78"></a> `008def78` | `a3 36 ee 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-008def7c"></a> `008def7c` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-008def80"></a> `008def80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008def84"></a> `008def84` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-008def88"></a> `008def88` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-008def8c"></a> `008def8c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-008def90"></a> `008def90` | `e5 06 80 52` | mov w5,#0x37 | `FALL_THROUGH`
<a id="insn-008def94"></a> `008def94` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-008def98"></a> `008def98` | `2b 2b ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008def9c"></a> `008def9c` | `48 ab 44 b9` | ldr w8,[x26, #0x4a8] | `FALL_THROUGH`
<a id="insn-008defa0"></a> `008defa0` | `1f a1 04 71` | cmp w8,#0x128 | `FALL_THROUGH`
<a id="insn-008defa4"></a> `008defa4` | `0c 01 00 54` | b.gt 0x008defc4 | `CONDITIONAL_JUMP`
<a id="insn-008defa8"></a> `008defa8` | `81 fe 40 f9` | ldr x1,[x20, #0x1f8] | `FALL_THROUGH`
<a id="insn-008defac"></a> `008defac` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-008defb0"></a> `008defb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008defb4"></a> `008defb4` | `22 01 08 4b` | sub w2,w9,w8 | `FALL_THROUGH`
<a id="insn-008defb8"></a> `008defb8` | `63 00 80 52` | mov w3,#0x3 | `FALL_THROUGH`
<a id="insn-008defbc"></a> `008defbc` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-008defc0"></a> `008defc0` | `02 28 ee 97` | bl 0x00468fc8 | `UNCONDITIONAL_CALL`
<a id="insn-008defc4"></a> `008defc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008defc8"></a> `008defc8` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-008defcc"></a> `008defcc` | `35 27 ee 97` | bl 0x00468ca0 | `UNCONDITIONAL_CALL`
<a id="insn-008defd0"></a> `008defd0` | `97 66 40 f9` | ldr x23,[x20, #0xc8] | `FALL_THROUGH`
<a id="insn-008defd4"></a> `008defd4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008defd8"></a> `008defd8` | `8b 36 ee 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-008defdc"></a> `008defdc` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-008defe0"></a> `008defe0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008defe4"></a> `008defe4` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-008defe8"></a> `008defe8` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-008defec"></a> `008defec` | `23 49 80 52` | mov w3,#0x249 | `FALL_THROUGH`
<a id="insn-008deff0"></a> `008deff0` | `e5 06 80 52` | mov w5,#0x37 | `FALL_THROUGH`
<a id="insn-008deff4"></a> `008deff4` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-008deff8"></a> `008deff8` | `13 2b ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008deffc"></a> `008deffc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df000"></a> `008df000` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-008df004"></a> `008df004` | `27 27 ee 97` | bl 0x00468ca0 | `UNCONDITIONAL_CALL`
<a id="insn-008df008"></a> `008df008` | `f8 1d 00 90` | adrp x24,0xc9b000 | `FALL_THROUGH`
<a id="insn-008df00c"></a> `008df00c` | `48 f7 80 b9` | ldrsw x8,[x26, #0xf4] | `FALL_THROUGH`
<a id="insn-008df010"></a> `008df010` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df014"></a> `008df014` | `18 bf 42 f9` | ldr x24,[x24, #0x578] | `FALL_THROUGH`
<a id="insn-008df018"></a> `008df018` | `81 56 40 f9` | ldr x1,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-008df01c"></a> `008df01c` | `26 01 80 52` | mov w6,#0x9 | `FALL_THROUGH`
<a id="insn-008df020"></a> `008df020` | `4a 2f 40 29` | ldp w10,w11,[x26] | `FALL_THROUGH`
<a id="insn-008df024"></a> `008df024` | `08 7b 68 b8` | ldr w8,[x24, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-008df028"></a> `008df028` | `4c 37 41 29` | ldp w12,w13,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-008df02c"></a> `008df02c` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-008df030"></a> `008df030` | `09 a5 88 1a` | cinc w9,w8,lt | `FALL_THROUGH`
<a id="insn-008df034"></a> `008df034` | `29 7d 01 13` | asr w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-008df038"></a> `008df038` | `84 01 08 0b` | add w4,w12,w8 | `FALL_THROUGH`
<a id="insn-008df03c"></a> `008df03c` | `a5 01 08 0b` | add w5,w13,w8 | `FALL_THROUGH`
<a id="insn-008df040"></a> `008df040` | `42 01 09 4b` | sub w2,w10,w9 | `FALL_THROUGH`
<a id="insn-008df044"></a> `008df044` | `63 01 09 4b` | sub w3,w11,w9 | `FALL_THROUGH`
<a id="insn-008df048"></a> `008df048` | `ff 2a ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008df04c"></a> `008df04c` | `48 f7 80 b9` | ldrsw x8,[x26, #0xf4] | `FALL_THROUGH`
<a id="insn-008df050"></a> `008df050` | `81 56 40 f9` | ldr x1,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-008df054"></a> `008df054` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df058"></a> `008df058` | `4a 2f 40 29` | ldp w10,w11,[x26] | `FALL_THROUGH`
<a id="insn-008df05c"></a> `008df05c` | `08 7b 68 b8` | ldr w8,[x24, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-008df060"></a> `008df060` | `66 00 80 52` | mov w6,#0x3 | `FALL_THROUGH`
<a id="insn-008df064"></a> `008df064` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-008df068"></a> `008df068` | `04 51 01 11` | add w4,w8,#0x54 | `FALL_THROUGH`
<a id="insn-008df06c"></a> `008df06c` | `05 f1 00 11` | add w5,w8,#0x3c | `FALL_THROUGH`
<a id="insn-008df070"></a> `008df070` | `09 a5 88 1a` | cinc w9,w8,lt | `FALL_THROUGH`
<a id="insn-008df074"></a> `008df074` | `29 7d 01 13` | asr w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-008df078"></a> `008df078` | `4a 01 09 4b` | sub w10,w10,w9 | `FALL_THROUGH`
<a id="insn-008df07c"></a> `008df07c` | `69 01 09 4b` | sub w9,w11,w9 | `FALL_THROUGH`
<a id="insn-008df080"></a> `008df080` | `42 11 00 11` | add w2,w10,#0x4 | `FALL_THROUGH`
<a id="insn-008df084"></a> `008df084` | `23 45 00 11` | add w3,w9,#0x11 | `FALL_THROUGH`
<a id="insn-008df088"></a> `008df088` | `ef 2a ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008df08c"></a> `008df08c` | `68 13 67 39` | ldrb w8,[x27, #0x9c4] | `FALL_THROUGH`
<a id="insn-008df090"></a> `008df090` | `28 02 00 37` | tbnz w8,#0x0,0x008df0d4 | `CONDITIONAL_JUMP`
<a id="insn-008df094"></a> `008df094` | `68 17 67 39` | ldrb w8,[x27, #0x9c5] | `FALL_THROUGH`
<a id="insn-008df098"></a> `008df098` | `e8 01 00 37` | tbnz w8,#0x0,0x008df0d4 | `CONDITIONAL_JUMP`
<a id="insn-008df09c"></a> `008df09c` | `68 37 67 39` | ldrb w8,[x27, #0x9cd] | `FALL_THROUGH`
<a id="insn-008df0a0"></a> `008df0a0` | `28 01 00 37` | tbnz w8,#0x0,0x008df0c4 | `CONDITIONAL_JUMP`
<a id="insn-008df0a4"></a> `008df0a4` | `68 27 67 39` | ldrb w8,[x27, #0x9c9] | `FALL_THROUGH`
<a id="insn-008df0a8"></a> `008df0a8` | `e8 00 00 37` | tbnz w8,#0x0,0x008df0c4 | `CONDITIONAL_JUMP`
<a id="insn-008df0ac"></a> `008df0ac` | `68 47 67 39` | ldrb w8,[x27, #0x9d1] | `FALL_THROUGH`
<a id="insn-008df0b0"></a> `008df0b0` | `a8 00 00 37` | tbnz w8,#0x0,0x008df0c4 | `CONDITIONAL_JUMP`
<a id="insn-008df0b4"></a> `008df0b4` | `68 1b 67 39` | ldrb w8,[x27, #0x9c6] | `FALL_THROUGH`
<a id="insn-008df0b8"></a> `008df0b8` | `68 00 00 37` | tbnz w8,#0x0,0x008df0c4 | `CONDITIONAL_JUMP`
<a id="insn-008df0bc"></a> `008df0bc` | `68 03 40 39` | ldrb w8,[x27] | `FALL_THROUGH`
<a id="insn-008df0c0"></a> `008df0c0` | `a8 14 00 36` | tbz w8,#0x0,0x008df354 | `CONDITIONAL_JUMP`
<a id="insn-008df0c4"></a> `008df0c4` | `68 17 67 39` | ldrb w8,[x27, #0x9c5] | `FALL_THROUGH`
<a id="insn-008df0c8"></a> `008df0c8` | `68 00 00 35` | cbnz w8,0x008df0d4 | `CONDITIONAL_JUMP`
<a id="insn-008df0cc"></a> `008df0cc` | `68 47 67 39` | ldrb w8,[x27, #0x9d1] | `FALL_THROUGH`
<a id="insn-008df0d0"></a> `008df0d0` | `48 05 00 34` | cbz w8,0x008df178 | `CONDITIONAL_JUMP`
<a id="insn-008df0d4"></a> `008df0d4` | `81 7e 40 f9` | ldr x1,[x20, #0xf8] | `FALL_THROUGH`
<a id="insn-008df0d8"></a> `008df0d8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df0dc"></a> `008df0dc` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-008df0e0"></a> `008df0e0` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-008df0e4"></a> `008df0e4` | `64 01 80 52` | mov w4,#0xb | `FALL_THROUGH`
<a id="insn-008df0e8"></a> `008df0e8` | `b8 27 ee 97` | bl 0x00468fc8 | `UNCONDITIONAL_CALL`
<a id="insn-008df0ec"></a> `008df0ec` | `81 7e 40 f9` | ldr x1,[x20, #0xf8] | `FALL_THROUGH`
<a id="insn-008df0f0"></a> `008df0f0` | `c2 92 01 51` | sub w2,w22,#0x64 | `FALL_THROUGH`
<a id="insn-008df0f4"></a> `008df0f4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df0f8"></a> `008df0f8` | `23 02 80 52` | mov w3,#0x11 | `FALL_THROUGH`
<a id="insn-008df0fc"></a> `008df0fc` | `44 01 80 52` | mov w4,#0xa | `FALL_THROUGH`
<a id="insn-008df100"></a> `008df100` | `b2 27 ee 97` | bl 0x00468fc8 | `UNCONDITIONAL_CALL`
<a id="insn-008df104"></a> `008df104` | `97 7e 40 f9` | ldr x23,[x20, #0xf8] | `FALL_THROUGH`
<a id="insn-008df108"></a> `008df108` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008df10c"></a> `008df10c` | `3e 36 ee 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-008df110"></a> `008df110` | `08 18 00 51` | sub w8,w0,#0x6 | `FALL_THROUGH`
<a id="insn-008df114"></a> `008df114` | `08 01 22 1e` | scvtf s8,w8 | `FALL_THROUGH`
<a id="insn-008df118"></a> `008df118` | `08 ae 98 52` | mov w8,#0xc570 | `FALL_THROUGH`
<a id="insn-008df11c"></a> `008df11c` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-008df120"></a> `008df120` | `84 73 09 94` | bl 0x00b3bf30 | `UNCONDITIONAL_CALL`
<a id="insn-008df124"></a> `008df124` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-008df128"></a> `008df128` | `01 10 23 1e` | fmov s1,0x40c00000 | `FALL_THROUGH`
<a id="insn-008df12c"></a> `008df12c` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-008df130"></a> `008df130` | `02 10 3e 1e` | fmov s2,0xbf800000 | `FALL_THROUGH`
<a id="insn-008df134"></a> `008df134` | `e8 13 00 91` | add x8,sp,#0x4 | `FALL_THROUGH`
<a id="insn-008df138"></a> `008df138` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df13c"></a> `008df13c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-008df140"></a> `008df140` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-008df144"></a> `008df144` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-008df148"></a> `008df148` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-008df14c"></a> `008df14c` | `46 00 80 52` | mov w6,#0x2 | `FALL_THROUGH`
<a id="insn-008df150"></a> `008df150` | `e7 03 1f 2a` | mov w7,wzr | `FALL_THROUGH`
<a id="insn-008df154"></a> `008df154` | `7e 2f ee 97` | bl 0x0046af4c | `UNCONDITIONAL_CALL`
<a id="insn-008df158"></a> `008df158` | `81 56 40 f9` | ldr x1,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-008df15c"></a> `008df15c` | `c2 96 00 51` | sub w2,w22,#0x25 | `FALL_THROUGH`
<a id="insn-008df160"></a> `008df160` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df164"></a> `008df164` | `03 01 80 52` | mov w3,#0x8 | `FALL_THROUGH`
<a id="insn-008df168"></a> `008df168` | `c4 07 80 52` | mov w4,#0x3e | `FALL_THROUGH`
<a id="insn-008df16c"></a> `008df16c` | `85 04 80 52` | mov w5,#0x24 | `FALL_THROUGH`
<a id="insn-008df170"></a> `008df170` | `e6 02 80 52` | mov w6,#0x17 | `FALL_THROUGH`
<a id="insn-008df174"></a> `008df174` | `b4 2a ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008df178"></a> `008df178` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df17c"></a> `008df17c` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-008df180"></a> `008df180` | `c8 26 ee 97` | bl 0x00468ca0 | `UNCONDITIONAL_CALL`
<a id="insn-008df184"></a> `008df184` | `81 7e 40 f9` | ldr x1,[x20, #0xf8] | `FALL_THROUGH`
<a id="insn-008df188"></a> `008df188` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df18c"></a> `008df18c` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-008df190"></a> `008df190` | `23 49 80 52` | mov w3,#0x249 | `FALL_THROUGH`
<a id="insn-008df194"></a> `008df194` | `64 01 80 52` | mov w4,#0xb | `FALL_THROUGH`
<a id="insn-008df198"></a> `008df198` | `8c 27 ee 97` | bl 0x00468fc8 | `UNCONDITIONAL_CALL`
<a id="insn-008df19c"></a> `008df19c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df1a0"></a> `008df1a0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-008df1a4"></a> `008df1a4` | `bf 26 ee 97` | bl 0x00468ca0 | `UNCONDITIONAL_CALL`
<a id="insn-008df1a8"></a> `008df1a8` | `82 56 40 f9` | ldr x2,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-008df1ac"></a> `008df1ac` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008df1b0"></a> `008df1b0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-008df1b4"></a> `008df1b4` | `e3 03 16 2a` | mov w3,w22 | `FALL_THROUGH`
<a id="insn-008df1b8"></a> `008df1b8` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-008df1bc"></a> `008df1bc` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-008df1c0"></a> `008df1c0` | `51 72 fa 97` | bl 0x0077bb04 | `UNCONDITIONAL_CALL`
<a id="insn-008df1c4"></a> `008df1c4` | `96 7e 40 f9` | ldr x22,[x20, #0xf8] | `FALL_THROUGH`
<a id="insn-008df1c8"></a> `008df1c8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008df1cc"></a> `008df1cc` | `0e 36 ee 97` | bl 0x0046ca04 | `UNCONDITIONAL_CALL`
<a id="insn-008df1d0"></a> `008df1d0` | `08 18 00 51` | sub w8,w0,#0x6 | `FALL_THROUGH`
<a id="insn-008df1d4"></a> `008df1d4` | `08 01 22 1e` | scvtf s8,w8 | `FALL_THROUGH`
<a id="insn-008df1d8"></a> `008df1d8` | `08 80 98 52` | mov w8,#0xc400 | `FALL_THROUGH`
<a id="insn-008df1dc"></a> `008df1dc` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-008df1e0"></a> `008df1e0` | `54 73 09 94` | bl 0x00b3bf30 | `UNCONDITIONAL_CALL`
<a id="insn-008df1e4"></a> `008df1e4` | `89 82 a8 52` | mov w9,#0x44140000 | `FALL_THROUGH`
<a id="insn-008df1e8"></a> `008df1e8` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-008df1ec"></a> `008df1ec` | `02 10 3e 1e` | fmov s2,0xbf800000 | `FALL_THROUGH`
<a id="insn-008df1f0"></a> `008df1f0` | `21 01 27 1e` | fmov s1,w9 | `FALL_THROUGH`
<a id="insn-008df1f4"></a> `008df1f4` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-008df1f8"></a> `008df1f8` | `e8 13 00 91` | add x8,sp,#0x4 | `FALL_THROUGH`
<a id="insn-008df1fc"></a> `008df1fc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df200"></a> `008df200` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-008df204"></a> `008df204` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-008df208"></a> `008df208` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-008df20c"></a> `008df20c` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-008df210"></a> `008df210` | `46 00 80 52` | mov w6,#0x2 | `FALL_THROUGH`
<a id="insn-008df214"></a> `008df214` | `e7 03 1f 2a` | mov w7,wzr | `FALL_THROUGH`
<a id="insn-008df218"></a> `008df218` | `4d 2f ee 97` | bl 0x0046af4c | `UNCONDITIONAL_CALL`
<a id="insn-008df21c"></a> `008df21c` | `48 f7 80 b9` | ldrsw x8,[x26, #0xf4] | `FALL_THROUGH`
<a id="insn-008df220"></a> `008df220` | `81 56 40 f9` | ldr x1,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-008df224"></a> `008df224` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df228"></a> `008df228` | `4a 2f 40 29` | ldp w10,w11,[x26] | `FALL_THROUGH`
<a id="insn-008df22c"></a> `008df22c` | `08 7b 68 b8` | ldr w8,[x24, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-008df230"></a> `008df230` | `26 01 80 52` | mov w6,#0x9 | `FALL_THROUGH`
<a id="insn-008df234"></a> `008df234` | `4c 37 41 29` | ldp w12,w13,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-008df238"></a> `008df238` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-008df23c"></a> `008df23c` | `09 a5 88 1a` | cinc w9,w8,lt | `FALL_THROUGH`
<a id="insn-008df240"></a> `008df240` | `29 7d 01 13` | asr w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-008df244"></a> `008df244` | `84 01 08 0b` | add w4,w12,w8 | `FALL_THROUGH`
<a id="insn-008df248"></a> `008df248` | `a5 01 08 0b` | add w5,w13,w8 | `FALL_THROUGH`
<a id="insn-008df24c"></a> `008df24c` | `42 01 09 4b` | sub w2,w10,w9 | `FALL_THROUGH`
<a id="insn-008df250"></a> `008df250` | `63 01 09 4b` | sub w3,w11,w9 | `FALL_THROUGH`
<a id="insn-008df254"></a> `008df254` | `7c 2a ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008df258"></a> `008df258` | `48 f7 80 b9` | ldrsw x8,[x26, #0xf4] | `FALL_THROUGH`
<a id="insn-008df25c"></a> `008df25c` | `81 56 40 f9` | ldr x1,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-008df260"></a> `008df260` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df264"></a> `008df264` | `4a 2f 40 29` | ldp w10,w11,[x26] | `FALL_THROUGH`
<a id="insn-008df268"></a> `008df268` | `08 7b 68 b8` | ldr w8,[x24, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-008df26c"></a> `008df26c` | `66 00 80 52` | mov w6,#0x3 | `FALL_THROUGH`
<a id="insn-008df270"></a> `008df270` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-008df274"></a> `008df274` | `04 51 01 11` | add w4,w8,#0x54 | `FALL_THROUGH`
<a id="insn-008df278"></a> `008df278` | `05 f1 00 11` | add w5,w8,#0x3c | `FALL_THROUGH`
<a id="insn-008df27c"></a> `008df27c` | `09 a5 88 1a` | cinc w9,w8,lt | `FALL_THROUGH`
<a id="insn-008df280"></a> `008df280` | `29 7d 01 13` | asr w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-008df284"></a> `008df284` | `4a 01 09 4b` | sub w10,w10,w9 | `FALL_THROUGH`
<a id="insn-008df288"></a> `008df288` | `69 01 09 4b` | sub w9,w11,w9 | `FALL_THROUGH`
<a id="insn-008df28c"></a> `008df28c` | `42 11 00 11` | add w2,w10,#0x4 | `FALL_THROUGH`
<a id="insn-008df290"></a> `008df290` | `23 45 00 11` | add w3,w9,#0x11 | `FALL_THROUGH`
<a id="insn-008df294"></a> `008df294` | `6c 2a ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008df298"></a> `008df298` | `68 13 67 39` | ldrb w8,[x27, #0x9c4] | `FALL_THROUGH`
<a id="insn-008df29c"></a> `008df29c` | `28 04 00 37` | tbnz w8,#0x0,0x008df320 | `CONDITIONAL_JUMP`
<a id="insn-008df2a0"></a> `008df2a0` | `68 17 67 39` | ldrb w8,[x27, #0x9c5] | `FALL_THROUGH`
<a id="insn-008df2a4"></a> `008df2a4` | `e8 03 00 37` | tbnz w8,#0x0,0x008df320 | `CONDITIONAL_JUMP`
<a id="insn-008df2a8"></a> `008df2a8` | `68 37 67 39` | ldrb w8,[x27, #0x9cd] | `FALL_THROUGH`
<a id="insn-008df2ac"></a> `008df2ac` | `a8 03 00 37` | tbnz w8,#0x0,0x008df320 | `CONDITIONAL_JUMP`
<a id="insn-008df2b0"></a> `008df2b0` | `68 27 67 39` | ldrb w8,[x27, #0x9c9] | `FALL_THROUGH`
<a id="insn-008df2b4"></a> `008df2b4` | `68 03 00 37` | tbnz w8,#0x0,0x008df320 | `CONDITIONAL_JUMP`
<a id="insn-008df2b8"></a> `008df2b8` | `68 47 67 39` | ldrb w8,[x27, #0x9d1] | `FALL_THROUGH`
<a id="insn-008df2bc"></a> `008df2bc` | `28 03 00 37` | tbnz w8,#0x0,0x008df320 | `CONDITIONAL_JUMP`
<a id="insn-008df2c0"></a> `008df2c0` | `68 1b 67 39` | ldrb w8,[x27, #0x9c6] | `FALL_THROUGH`
<a id="insn-008df2c4"></a> `008df2c4` | `e8 02 00 37` | tbnz w8,#0x0,0x008df320 | `CONDITIONAL_JUMP`
<a id="insn-008df2c8"></a> `008df2c8` | `68 03 40 39` | ldrb w8,[x27] | `FALL_THROUGH`
<a id="insn-008df2cc"></a> `008df2cc` | `a8 02 00 37` | tbnz w8,#0x0,0x008df320 | `CONDITIONAL_JUMP`
<a id="insn-008df2d0"></a> `008df2d0` | `68 3b 67 39` | ldrb w8,[x27, #0x9ce] | `FALL_THROUGH`
<a id="insn-008df2d4"></a> `008df2d4` | `68 02 00 34` | cbz w8,0x008df320 | `CONDITIONAL_JUMP`
<a id="insn-008df2d8"></a> `008df2d8` | `48 cf 42 b9` | ldr w8,[x26, #0x2cc] | `FALL_THROUGH`
<a id="insn-008df2dc"></a> `008df2dc` | `81 56 40 f9` | ldr x1,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-008df2e0"></a> `008df2e0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df2e4"></a> `008df2e4` | `62 00 80 52` | mov w2,#0x3 | `FALL_THROUGH`
<a id="insn-008df2e8"></a> `008df2e8` | `83 43 80 52` | mov w3,#0x21c | `FALL_THROUGH`
<a id="insn-008df2ec"></a> `008df2ec` | `04 0c 80 52` | mov w4,#0x60 | `FALL_THROUGH`
<a id="insn-008df2f0"></a> `008df2f0` | `e9 03 08 6b` | negs w9,w8 | `FALL_THROUGH`
<a id="insn-008df2f4"></a> `008df2f4` | `08 05 00 12` | and w8,w8,#0x3 | `FALL_THROUGH`
<a id="insn-008df2f8"></a> `008df2f8` | `05 0c 80 52` | mov w5,#0x60 | `FALL_THROUGH`
<a id="insn-008df2fc"></a> `008df2fc` | `29 05 00 12` | and w9,w9,#0x3 | `FALL_THROUGH`
<a id="insn-008df300"></a> `008df300` | `08 45 89 5a` | csneg w8,w8,w9,mi | `FALL_THROUGH`
<a id="insn-008df304"></a> `008df304` | `09 01 19 12` | and w9,w8,#0x80 | `FALL_THROUGH`
<a id="insn-008df308"></a> `008df308` | `08 1d 49 0b` | add w8,w8,w9, LSR #0x7 | `FALL_THROUGH`
<a id="insn-008df30c"></a> `008df30c` | `08 1d 00 13` | sxtb w8,w8 | `FALL_THROUGH`
<a id="insn-008df310"></a> `008df310` | `08 7d 01 53` | lsr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-008df314"></a> `008df314` | `08 31 00 11` | add w8,w8,#0xc | `FALL_THROUGH`
<a id="insn-008df318"></a> `008df318` | `06 1d 00 12` | and w6,w8,#0xff | `FALL_THROUGH`
<a id="insn-008df31c"></a> `008df31c` | `4a 2a ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008df320"></a> `008df320` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-008df324"></a> `008df324` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-008df328"></a> `008df328` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008df32c"></a> `008df32c` | `21 07 00 54` | b.ne 0x008df410 | `CONDITIONAL_JUMP`
<a id="insn-008df330"></a> `008df330` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-008df334"></a> `008df334` | `fb 1f 40 f9` | ldr x27,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-008df338"></a> `008df338` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008df33c"></a> `008df33c` | `e8 13 40 fd` | ldr d8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-008df340"></a> `008df340` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-008df344"></a> `008df344` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-008df348"></a> `008df348` | `fd fb 42 a9` | ldp x29,x30,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-008df34c"></a> `008df34c` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-008df350"></a> `008df350` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008df354"></a> `008df354` | `68 3b 67 39` | ldrb w8,[x27, #0x9ce] | `FALL_THROUGH`
<a id="insn-008df358"></a> `008df358` | `68 eb ff 34` | cbz w8,0x008df0c4 | `CONDITIONAL_JUMP`
<a id="insn-008df35c"></a> `008df35c` | `48 cf 42 b9` | ldr w8,[x26, #0x2cc] | `FALL_THROUGH`
<a id="insn-008df360"></a> `008df360` | `81 56 40 f9` | ldr x1,[x20, #0xa8] | `FALL_THROUGH`
<a id="insn-008df364"></a> `008df364` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008df368"></a> `008df368` | `62 00 80 52` | mov w2,#0x3 | `FALL_THROUGH`
<a id="insn-008df36c"></a> `008df36c` | `83 43 80 52` | mov w3,#0x21c | `FALL_THROUGH`
<a id="insn-008df370"></a> `008df370` | `04 0c 80 52` | mov w4,#0x60 | `FALL_THROUGH`
<a id="insn-008df374"></a> `008df374` | `e9 03 08 6b` | negs w9,w8 | `FALL_THROUGH`
<a id="insn-008df378"></a> `008df378` | `08 05 00 12` | and w8,w8,#0x3 | `FALL_THROUGH`
<a id="insn-008df37c"></a> `008df37c` | `05 0c 80 52` | mov w5,#0x60 | `FALL_THROUGH`
<a id="insn-008df380"></a> `008df380` | `29 05 00 12` | and w9,w9,#0x3 | `FALL_THROUGH`
<a id="insn-008df384"></a> `008df384` | `08 45 89 5a` | csneg w8,w8,w9,mi | `FALL_THROUGH`
<a id="insn-008df388"></a> `008df388` | `09 01 19 12` | and w9,w8,#0x80 | `FALL_THROUGH`
<a id="insn-008df38c"></a> `008df38c` | `08 1d 49 0b` | add w8,w8,w9, LSR #0x7 | `FALL_THROUGH`
<a id="insn-008df390"></a> `008df390` | `08 1d 00 13` | sxtb w8,w8 | `FALL_THROUGH`
<a id="insn-008df394"></a> `008df394` | `08 7d 01 53` | lsr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-008df398"></a> `008df398` | `08 31 00 11` | add w8,w8,#0xc | `FALL_THROUGH`
<a id="insn-008df39c"></a> `008df39c` | `06 1d 00 12` | and w6,w8,#0xff | `FALL_THROUGH`
<a id="insn-008df3a0"></a> `008df3a0` | `29 2a ee 97` | bl 0x00469c44 | `UNCONDITIONAL_CALL`
<a id="insn-008df3a4"></a> `008df3a4` | `68 13 67 39` | ldrb w8,[x27, #0x9c4] | `FALL_THROUGH`
<a id="insn-008df3a8"></a> `008df3a8` | `69 17 67 39` | ldrb w9,[x27, #0x9c5] | `FALL_THROUGH`
<a id="insn-008df3ac"></a> `008df3ac` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-008df3b0"></a> `008df3b0` | `e8 e8 ff 34` | cbz w8,0x008df0cc | `CONDITIONAL_JUMP`
<a id="insn-008df3b4"></a> `008df3b4` | `48 ff ff 17` | b 0x008df0d4 | `UNCONDITIONAL_JUMP`
<a id="insn-008df3b8"></a> `008df3b8` | `20 1e 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008df3bc"></a> `008df3bc` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008df3c0"></a> `008df3c0` | `d8 e2 0d 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-008df3c4"></a> `008df3c4` | `80 b9 ff 34` | cbz w0,0x008deaf4 | `CONDITIONAL_JUMP`
<a id="insn-008df3c8"></a> `008df3c8` | `21 1e 00 d0` | adrp x1,0xca5000 | `FALL_THROUGH`
<a id="insn-008df3cc"></a> `008df3cc` | `21 00 00 91` | add x1,x1,#0x0 | `FALL_THROUGH`
<a id="insn-008df3d0"></a> `008df3d0` | `e0 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008df3d4"></a> `008df3d4` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-008df3d8"></a> `008df3d8` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-008df3dc"></a> `008df3dc` | `22 1c 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-008df3e0"></a> `008df3e0` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-008df3e4"></a> `008df3e4` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008df3e8"></a> `008df3e8` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-008df3ec"></a> `008df3ec` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-008df3f0"></a> `008df3f0` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-008df3f4"></a> `008df3f4` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008df3f8"></a> `008df3f8` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-008df3fc"></a> `008df3fc` | `c1 e2 0d 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-008df400"></a> `008df400` | `20 1e 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008df404"></a> `008df404` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008df408"></a> `008df408` | `ce e2 0d 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-008df40c"></a> `008df40c` | `ba fd ff 17` | b 0x008deaf4 | `UNCONDITIONAL_JUMP`
<a id="insn-008df410"></a> `008df410` | `e8 e2 0d 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`
<a id="insn-008df414"></a> `008df414` | `20 1e 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008df418"></a> `008df418` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008df41c"></a> `008df41c` | `c1 e2 0d 94` | bl 0x00c57f20 | `UNCONDITIONAL_CALL`
<a id="insn-008df420"></a> `008df420` | `c0 ba ff 34` | cbz w0,0x008deb78 | `CONDITIONAL_JUMP`
<a id="insn-008df424"></a> `008df424` | `21 1e 00 d0` | adrp x1,0xca5000 | `FALL_THROUGH`
<a id="insn-008df428"></a> `008df428` | `21 00 00 91` | add x1,x1,#0x0 | `FALL_THROUGH`
<a id="insn-008df42c"></a> `008df42c` | `e0 dc ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-008df430"></a> `008df430` | `00 d0 37 91` | add x0,x0,#0xdf4 | `FALL_THROUGH`
<a id="insn-008df434"></a> `008df434` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-008df438"></a> `008df438` | `22 1c 00 90` | adrp x2,0xc63000 | `FALL_THROUGH`
<a id="insn-008df43c"></a> `008df43c` | `42 80 01 91` | add x2,x2,#0x60 | `FALL_THROUGH`
<a id="insn-008df440"></a> `008df440` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-008df444"></a> `008df444` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-008df448"></a> `008df448` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-008df44c"></a> `008df44c` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-008df450"></a> `008df450` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-008df454"></a> `008df454` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-008df458"></a> `008df458` | `aa e2 0d 94` | bl 0x00c57f00 | `UNCONDITIONAL_CALL`
<a id="insn-008df45c"></a> `008df45c` | `20 1e 00 d0` | adrp x0,0xca5000 | `FALL_THROUGH`
<a id="insn-008df460"></a> `008df460` | `00 e0 00 91` | add x0,x0,#0x38 | `FALL_THROUGH`
<a id="insn-008df464"></a> `008df464` | `b7 e2 0d 94` | bl 0x00c57f40 | `UNCONDITIONAL_CALL`
<a id="insn-008df468"></a> `008df468` | `c4 fd ff 17` | b 0x008deb78 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`008deaac`](#insn-008deaac) 範囲 `[['008deaac', '008deaf3']]`
  - `CONDITIONAL_JUMP` [`008deaf0`](#insn-008deaf0) → [`008df3b8`](#insn-008df3b8)
  - `FALL_THROUGH` [`008deaf0`](#insn-008deaf0) → [`008deaf4`](#insn-008deaf4)
- ブロック [`008deaf4`](#insn-008deaf4) 範囲 `[['008deaf4', '008deaff']]`
  - `CONDITIONAL_JUMP` [`008deafc`](#insn-008deafc) → [`008deb04`](#insn-008deb04)
  - `FALL_THROUGH` [`008deafc`](#insn-008deafc) → [`008deb00`](#insn-008deb00)
- ブロック [`008deb00`](#insn-008deb00) 範囲 `[['008deb00', '008deb03']]`
  - `FALL_THROUGH` [`008deb00`](#insn-008deb00) → [`008deb04`](#insn-008deb04)
- ブロック [`008deb04`](#insn-008deb04) 範囲 `[['008deb04', '008deb1f']]`
  - `CONDITIONAL_JUMP` [`008deb1c`](#insn-008deb1c) → [`008deb40`](#insn-008deb40)
  - `FALL_THROUGH` [`008deb1c`](#insn-008deb1c) → [`008deb20`](#insn-008deb20)
- ブロック [`008deb20`](#insn-008deb20) 範囲 `[['008deb20', '008deb3f']]`
  - `UNCONDITIONAL_JUMP` [`008deb3c`](#insn-008deb3c) → [`008deb44`](#insn-008deb44)
- ブロック [`008deb40`](#insn-008deb40) 範囲 `[['008deb40', '008deb43']]`
  - `FALL_THROUGH` [`008deb40`](#insn-008deb40) → [`008deb44`](#insn-008deb44)
- ブロック [`008deb44`](#insn-008deb44) 範囲 `[['008deb44', '008deb6f']]`
  - `CONDITIONAL_JUMP` [`008deb6c`](#insn-008deb6c) → [`008deb88`](#insn-008deb88)
  - `FALL_THROUGH` [`008deb6c`](#insn-008deb6c) → [`008deb70`](#insn-008deb70)
- ブロック [`008deb70`](#insn-008deb70) 範囲 `[['008deb70', '008deb77']]`
  - `CONDITIONAL_JUMP` [`008deb74`](#insn-008deb74) → [`008df414`](#insn-008df414)
  - `FALL_THROUGH` [`008deb74`](#insn-008deb74) → [`008deb78`](#insn-008deb78)
- ブロック [`008deb78`](#insn-008deb78) 範囲 `[['008deb78', '008deb7f']]`
  - `CONDITIONAL_JUMP` [`008deb7c`](#insn-008deb7c) → [`008deb88`](#insn-008deb88)
  - `FALL_THROUGH` [`008deb7c`](#insn-008deb7c) → [`008deb80`](#insn-008deb80)
- ブロック [`008deb80`](#insn-008deb80) 範囲 `[['008deb80', '008deb87']]`
  - `CONDITIONAL_JUMP` [`008deb84`](#insn-008deb84) → [`008def30`](#insn-008def30)
  - `FALL_THROUGH` [`008deb84`](#insn-008deb84) → [`008deb88`](#insn-008deb88)
- ブロック [`008deb88`](#insn-008deb88) 範囲 `[['008deb88', '008debab']]`
  - `FALL_THROUGH` [`008deba8`](#insn-008deba8) → [`008debac`](#insn-008debac)
- ブロック [`008debac`](#insn-008debac) 範囲 `[['008debac', '008debcb']]`
  - `FALL_THROUGH` [`008debc8`](#insn-008debc8) → [`008debcc`](#insn-008debcc)
- ブロック [`008debcc`](#insn-008debcc) 範囲 `[['008debcc', '008debe7']]`
  - `FALL_THROUGH` [`008debe4`](#insn-008debe4) → [`008debe8`](#insn-008debe8)
- ブロック [`008debe8`](#insn-008debe8) 範囲 `[['008debe8', '008decf7']]`
  - `CONDITIONAL_JUMP` [`008decf4`](#insn-008decf4) → [`008ded40`](#insn-008ded40)
  - `FALL_THROUGH` [`008decf4`](#insn-008decf4) → [`008decf8`](#insn-008decf8)
- ブロック [`008decf8`](#insn-008decf8) 範囲 `[['008decf8', '008ded3f']]`
  - `FALL_THROUGH` [`008ded3c`](#insn-008ded3c) → [`008ded40`](#insn-008ded40)
- ブロック [`008ded40`](#insn-008ded40) 範囲 `[['008ded40', '008ded6f']]`
  - `CONDITIONAL_JUMP` [`008ded6c`](#insn-008ded6c) → [`008dedc4`](#insn-008dedc4)
  - `FALL_THROUGH` [`008ded6c`](#insn-008ded6c) → [`008ded70`](#insn-008ded70)
- ブロック [`008ded70`](#insn-008ded70) 範囲 `[['008ded70', '008dedc3']]`
  - `FALL_THROUGH` [`008dedc0`](#insn-008dedc0) → [`008dedc4`](#insn-008dedc4)
- ブロック [`008dedc4`](#insn-008dedc4) 範囲 `[['008dedc4', '008dede7']]`
  - `CONDITIONAL_JUMP` [`008dede4`](#insn-008dede4) → [`008dee04`](#insn-008dee04)
  - `FALL_THROUGH` [`008dede4`](#insn-008dede4) → [`008dede8`](#insn-008dede8)
- ブロック [`008dede8`](#insn-008dede8) 範囲 `[['008dede8', '008dee03']]`
  - `FALL_THROUGH` [`008dee00`](#insn-008dee00) → [`008dee04`](#insn-008dee04)
- ブロック [`008dee04`](#insn-008dee04) 範囲 `[['008dee04', '008dee0b']]`
  - `CONDITIONAL_JUMP` [`008dee08`](#insn-008dee08) → [`008dee8c`](#insn-008dee8c)
  - `FALL_THROUGH` [`008dee08`](#insn-008dee08) → [`008dee0c`](#insn-008dee0c)
- ブロック [`008dee0c`](#insn-008dee0c) 範囲 `[['008dee0c', '008dee13']]`
  - `CONDITIONAL_JUMP` [`008dee10`](#insn-008dee10) → [`008dee8c`](#insn-008dee8c)
  - `FALL_THROUGH` [`008dee10`](#insn-008dee10) → [`008dee14`](#insn-008dee14)
- ブロック [`008dee14`](#insn-008dee14) 範囲 `[['008dee14', '008dee1b']]`
  - `CONDITIONAL_JUMP` [`008dee18`](#insn-008dee18) → [`008dee8c`](#insn-008dee8c)
  - `FALL_THROUGH` [`008dee18`](#insn-008dee18) → [`008dee1c`](#insn-008dee1c)
- ブロック [`008dee1c`](#insn-008dee1c) 範囲 `[['008dee1c', '008dee23']]`
  - `CONDITIONAL_JUMP` [`008dee20`](#insn-008dee20) → [`008dee8c`](#insn-008dee8c)
  - `FALL_THROUGH` [`008dee20`](#insn-008dee20) → [`008dee24`](#insn-008dee24)
- ブロック [`008dee24`](#insn-008dee24) 範囲 `[['008dee24', '008dee2b']]`
  - `CONDITIONAL_JUMP` [`008dee28`](#insn-008dee28) → [`008dee8c`](#insn-008dee8c)
  - `FALL_THROUGH` [`008dee28`](#insn-008dee28) → [`008dee2c`](#insn-008dee2c)
- ブロック [`008dee2c`](#insn-008dee2c) 範囲 `[['008dee2c', '008dee33']]`
  - `CONDITIONAL_JUMP` [`008dee30`](#insn-008dee30) → [`008dee8c`](#insn-008dee8c)
  - `FALL_THROUGH` [`008dee30`](#insn-008dee30) → [`008dee34`](#insn-008dee34)
- ブロック [`008dee34`](#insn-008dee34) 範囲 `[['008dee34', '008dee3b']]`
  - `CONDITIONAL_JUMP` [`008dee38`](#insn-008dee38) → [`008dee8c`](#insn-008dee8c)
  - `FALL_THROUGH` [`008dee38`](#insn-008dee38) → [`008dee3c`](#insn-008dee3c)
- ブロック [`008dee3c`](#insn-008dee3c) 範囲 `[['008dee3c', '008dee43']]`
  - `CONDITIONAL_JUMP` [`008dee40`](#insn-008dee40) → [`008dee8c`](#insn-008dee8c)
  - `FALL_THROUGH` [`008dee40`](#insn-008dee40) → [`008dee44`](#insn-008dee44)
- ブロック [`008dee44`](#insn-008dee44) 範囲 `[['008dee44', '008dee8b']]`
  - `FALL_THROUGH` [`008dee88`](#insn-008dee88) → [`008dee8c`](#insn-008dee8c)
- ブロック [`008dee8c`](#insn-008dee8c) 範囲 `[['008dee8c', '008deeb3']]`
  - `FALL_THROUGH` [`008deeb0`](#insn-008deeb0) → [`008deeb4`](#insn-008deeb4)
- ブロック [`008deeb4`](#insn-008deeb4) 範囲 `[['008deeb4', '008deec3']]`
  - `FALL_THROUGH` [`008deec0`](#insn-008deec0) → [`008deec4`](#insn-008deec4)
- ブロック [`008deec4`](#insn-008deec4) 範囲 `[['008deec4', '008deee3']]`
  - `FALL_THROUGH` [`008deee0`](#insn-008deee0) → [`008deee4`](#insn-008deee4)
- ブロック [`008deee4`](#insn-008deee4) 範囲 `[['008deee4', '008def2f']]`
  - `FALL_THROUGH` [`008def2c`](#insn-008def2c) → [`008def30`](#insn-008def30)
- ブロック [`008def30`](#insn-008def30) 範囲 `[['008def30', '008def4b']]`
  - `CONDITIONAL_JUMP` [`008def48`](#insn-008def48) → [`008def5c`](#insn-008def5c)
  - `FALL_THROUGH` [`008def48`](#insn-008def48) → [`008def4c`](#insn-008def4c)
- ブロック [`008def4c`](#insn-008def4c) 範囲 `[['008def4c', '008def53']]`
  - `CONDITIONAL_JUMP` [`008def50`](#insn-008def50) → [`008def5c`](#insn-008def5c)
  - `FALL_THROUGH` [`008def50`](#insn-008def50) → [`008def54`](#insn-008def54)
- ブロック [`008def54`](#insn-008def54) 範囲 `[['008def54', '008def5b']]`
  - `CONDITIONAL_JUMP` [`008def58`](#insn-008def58) → [`008defc4`](#insn-008defc4)
  - `FALL_THROUGH` [`008def58`](#insn-008def58) → [`008def5c`](#insn-008def5c)
- ブロック [`008def5c`](#insn-008def5c) 範囲 `[['008def5c', '008defa7']]`
  - `CONDITIONAL_JUMP` [`008defa4`](#insn-008defa4) → [`008defc4`](#insn-008defc4)
  - `FALL_THROUGH` [`008defa4`](#insn-008defa4) → [`008defa8`](#insn-008defa8)
- ブロック [`008defa8`](#insn-008defa8) 範囲 `[['008defa8', '008defc3']]`
  - `FALL_THROUGH` [`008defc0`](#insn-008defc0) → [`008defc4`](#insn-008defc4)
- ブロック [`008defc4`](#insn-008defc4) 範囲 `[['008defc4', '008defe3']]`
  - `FALL_THROUGH` [`008defe0`](#insn-008defe0) → [`008defe4`](#insn-008defe4)
- ブロック [`008defe4`](#insn-008defe4) 範囲 `[['008defe4', '008deff3']]`
  - `FALL_THROUGH` [`008deff0`](#insn-008deff0) → [`008deff4`](#insn-008deff4)
- ブロック [`008deff4`](#insn-008deff4) 範囲 `[['008deff4', '008deffb']]`
  - `FALL_THROUGH` [`008deff8`](#insn-008deff8) → [`008deffc`](#insn-008deffc)
- ブロック [`008deffc`](#insn-008deffc) 範囲 `[['008deffc', '008df01f']]`
  - `FALL_THROUGH` [`008df01c`](#insn-008df01c) → [`008df020`](#insn-008df020)
- ブロック [`008df020`](#insn-008df020) 範囲 `[['008df020', '008df027']]`
  - `FALL_THROUGH` [`008df024`](#insn-008df024) → [`008df028`](#insn-008df028)
- ブロック [`008df028`](#insn-008df028) 範囲 `[['008df028', '008df07b']]`
  - `FALL_THROUGH` [`008df078`](#insn-008df078) → [`008df07c`](#insn-008df07c)
- ブロック [`008df07c`](#insn-008df07c) 範囲 `[['008df07c', '008df093']]`
  - `CONDITIONAL_JUMP` [`008df090`](#insn-008df090) → [`008df0d4`](#insn-008df0d4)
  - `FALL_THROUGH` [`008df090`](#insn-008df090) → [`008df094`](#insn-008df094)
- ブロック [`008df094`](#insn-008df094) 範囲 `[['008df094', '008df09b']]`
  - `CONDITIONAL_JUMP` [`008df098`](#insn-008df098) → [`008df0d4`](#insn-008df0d4)
  - `FALL_THROUGH` [`008df098`](#insn-008df098) → [`008df09c`](#insn-008df09c)
- ブロック [`008df09c`](#insn-008df09c) 範囲 `[['008df09c', '008df0a3']]`
  - `CONDITIONAL_JUMP` [`008df0a0`](#insn-008df0a0) → [`008df0c4`](#insn-008df0c4)
  - `FALL_THROUGH` [`008df0a0`](#insn-008df0a0) → [`008df0a4`](#insn-008df0a4)
- ブロック [`008df0a4`](#insn-008df0a4) 範囲 `[['008df0a4', '008df0ab']]`
  - `CONDITIONAL_JUMP` [`008df0a8`](#insn-008df0a8) → [`008df0c4`](#insn-008df0c4)
  - `FALL_THROUGH` [`008df0a8`](#insn-008df0a8) → [`008df0ac`](#insn-008df0ac)
- ブロック [`008df0ac`](#insn-008df0ac) 範囲 `[['008df0ac', '008df0b3']]`
  - `CONDITIONAL_JUMP` [`008df0b0`](#insn-008df0b0) → [`008df0c4`](#insn-008df0c4)
  - `FALL_THROUGH` [`008df0b0`](#insn-008df0b0) → [`008df0b4`](#insn-008df0b4)
- ブロック [`008df0b4`](#insn-008df0b4) 範囲 `[['008df0b4', '008df0bb']]`
  - `CONDITIONAL_JUMP` [`008df0b8`](#insn-008df0b8) → [`008df0c4`](#insn-008df0c4)
  - `FALL_THROUGH` [`008df0b8`](#insn-008df0b8) → [`008df0bc`](#insn-008df0bc)
- ブロック [`008df0bc`](#insn-008df0bc) 範囲 `[['008df0bc', '008df0c3']]`
  - `CONDITIONAL_JUMP` [`008df0c0`](#insn-008df0c0) → [`008df354`](#insn-008df354)
  - `FALL_THROUGH` [`008df0c0`](#insn-008df0c0) → [`008df0c4`](#insn-008df0c4)
- ブロック [`008df0c4`](#insn-008df0c4) 範囲 `[['008df0c4', '008df0cb']]`
  - `CONDITIONAL_JUMP` [`008df0c8`](#insn-008df0c8) → [`008df0d4`](#insn-008df0d4)
  - `FALL_THROUGH` [`008df0c8`](#insn-008df0c8) → [`008df0cc`](#insn-008df0cc)
- ブロック [`008df0cc`](#insn-008df0cc) 範囲 `[['008df0cc', '008df0d3']]`
  - `CONDITIONAL_JUMP` [`008df0d0`](#insn-008df0d0) → [`008df178`](#insn-008df178)
  - `FALL_THROUGH` [`008df0d0`](#insn-008df0d0) → [`008df0d4`](#insn-008df0d4)
- ブロック [`008df0d4`](#insn-008df0d4) 範囲 `[['008df0d4', '008df0db']]`
  - `FALL_THROUGH` [`008df0d8`](#insn-008df0d8) → [`008df0dc`](#insn-008df0dc)
- ブロック [`008df0dc`](#insn-008df0dc) 範囲 `[['008df0dc', '008df10f']]`
  - `FALL_THROUGH` [`008df10c`](#insn-008df10c) → [`008df110`](#insn-008df110)
- ブロック [`008df110`](#insn-008df110) 範囲 `[['008df110', '008df13f']]`
  - `FALL_THROUGH` [`008df13c`](#insn-008df13c) → [`008df140`](#insn-008df140)
- ブロック [`008df140`](#insn-008df140) 範囲 `[['008df140', '008df177']]`
  - `FALL_THROUGH` [`008df174`](#insn-008df174) → [`008df178`](#insn-008df178)
- ブロック [`008df178`](#insn-008df178) 範囲 `[['008df178', '008df29f']]`
  - `CONDITIONAL_JUMP` [`008df29c`](#insn-008df29c) → [`008df320`](#insn-008df320)
  - `FALL_THROUGH` [`008df29c`](#insn-008df29c) → [`008df2a0`](#insn-008df2a0)
- ブロック [`008df2a0`](#insn-008df2a0) 範囲 `[['008df2a0', '008df2a7']]`
  - `CONDITIONAL_JUMP` [`008df2a4`](#insn-008df2a4) → [`008df320`](#insn-008df320)
  - `FALL_THROUGH` [`008df2a4`](#insn-008df2a4) → [`008df2a8`](#insn-008df2a8)
- ブロック [`008df2a8`](#insn-008df2a8) 範囲 `[['008df2a8', '008df2af']]`
  - `CONDITIONAL_JUMP` [`008df2ac`](#insn-008df2ac) → [`008df320`](#insn-008df320)
  - `FALL_THROUGH` [`008df2ac`](#insn-008df2ac) → [`008df2b0`](#insn-008df2b0)
- ブロック [`008df2b0`](#insn-008df2b0) 範囲 `[['008df2b0', '008df2b7']]`
  - `CONDITIONAL_JUMP` [`008df2b4`](#insn-008df2b4) → [`008df320`](#insn-008df320)
  - `FALL_THROUGH` [`008df2b4`](#insn-008df2b4) → [`008df2b8`](#insn-008df2b8)
- ブロック [`008df2b8`](#insn-008df2b8) 範囲 `[['008df2b8', '008df2bf']]`
  - `CONDITIONAL_JUMP` [`008df2bc`](#insn-008df2bc) → [`008df320`](#insn-008df320)
  - `FALL_THROUGH` [`008df2bc`](#insn-008df2bc) → [`008df2c0`](#insn-008df2c0)
- ブロック [`008df2c0`](#insn-008df2c0) 範囲 `[['008df2c0', '008df2c7']]`
  - `CONDITIONAL_JUMP` [`008df2c4`](#insn-008df2c4) → [`008df320`](#insn-008df320)
  - `FALL_THROUGH` [`008df2c4`](#insn-008df2c4) → [`008df2c8`](#insn-008df2c8)
- ブロック [`008df2c8`](#insn-008df2c8) 範囲 `[['008df2c8', '008df2cf']]`
  - `CONDITIONAL_JUMP` [`008df2cc`](#insn-008df2cc) → [`008df320`](#insn-008df320)
  - `FALL_THROUGH` [`008df2cc`](#insn-008df2cc) → [`008df2d0`](#insn-008df2d0)
- ブロック [`008df2d0`](#insn-008df2d0) 範囲 `[['008df2d0', '008df2d7']]`
  - `CONDITIONAL_JUMP` [`008df2d4`](#insn-008df2d4) → [`008df320`](#insn-008df320)
  - `FALL_THROUGH` [`008df2d4`](#insn-008df2d4) → [`008df2d8`](#insn-008df2d8)
- ブロック [`008df2d8`](#insn-008df2d8) 範囲 `[['008df2d8', '008df31f']]`
  - `FALL_THROUGH` [`008df31c`](#insn-008df31c) → [`008df320`](#insn-008df320)
- ブロック [`008df320`](#insn-008df320) 範囲 `[['008df320', '008df32f']]`
  - `CONDITIONAL_JUMP` [`008df32c`](#insn-008df32c) → [`008df410`](#insn-008df410)
  - `FALL_THROUGH` [`008df32c`](#insn-008df32c) → [`008df330`](#insn-008df330)
- ブロック [`008df330`](#insn-008df330) 範囲 `[['008df330', '008df353']]`
- ブロック [`008df354`](#insn-008df354) 範囲 `[['008df354', '008df35b']]`
  - `CONDITIONAL_JUMP` [`008df358`](#insn-008df358) → [`008df0c4`](#insn-008df0c4)
  - `FALL_THROUGH` [`008df358`](#insn-008df358) → [`008df35c`](#insn-008df35c)
- ブロック [`008df35c`](#insn-008df35c) 範囲 `[['008df35c', '008df3b3']]`
  - `CONDITIONAL_JUMP` [`008df3b0`](#insn-008df3b0) → [`008df0cc`](#insn-008df0cc)
  - `FALL_THROUGH` [`008df3b0`](#insn-008df3b0) → [`008df3b4`](#insn-008df3b4)
- ブロック [`008df3b4`](#insn-008df3b4) 範囲 `[['008df3b4', '008df3b7']]`
  - `UNCONDITIONAL_JUMP` [`008df3b4`](#insn-008df3b4) → [`008df0d4`](#insn-008df0d4)
- ブロック [`008df3b8`](#insn-008df3b8) 範囲 `[['008df3b8', '008df3c7']]`
  - `CONDITIONAL_JUMP` [`008df3c4`](#insn-008df3c4) → [`008deaf4`](#insn-008deaf4)
  - `FALL_THROUGH` [`008df3c4`](#insn-008df3c4) → [`008df3c8`](#insn-008df3c8)
- ブロック [`008df3c8`](#insn-008df3c8) 範囲 `[['008df3c8', '008df40f']]`
  - `UNCONDITIONAL_JUMP` [`008df40c`](#insn-008df40c) → [`008deaf4`](#insn-008deaf4)
- ブロック [`008df410`](#insn-008df410) 範囲 `[['008df410', '008df413']]`
- ブロック [`008df414`](#insn-008df414) 範囲 `[['008df414', '008df423']]`
  - `CONDITIONAL_JUMP` [`008df420`](#insn-008df420) → [`008deb78`](#insn-008deb78)
  - `FALL_THROUGH` [`008df420`](#insn-008df420) → [`008df424`](#insn-008df424)
- ブロック [`008df424`](#insn-008df424) 範囲 `[['008df424', '008df46b']]`
  - `UNCONDITIONAL_JUMP` [`008df468`](#insn-008df468) → [`008deb78`](#insn-008deb78)

## 命令位置別の参照

- [`008deab0`](#insn-008deab0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deab4`](#insn-008deab4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deab8`](#insn-008deab8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deabc`](#insn-008deabc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deac0`](#insn-008deac0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deac4`](#insn-008deac4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deac8`](#insn-008deac8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deae8`](#insn-008deae8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deaec`](#insn-008deaec) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008deaf0`](#insn-008deaf0) → [`008df3b8`](#insn-008df3b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deaf8`](#insn-008deaf8) → `00ca5030`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008deafc`](#insn-008deafc) → [`008deb04`](#insn-008deb04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deb00`](#insn-008deb00) → [`00498210`](../00498/00498210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00498210` · 推定シンボル `None` · 推定型 `None`
- [`008deb0c`](#insn-008deb0c) → `00ca4a78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008deb1c`](#insn-008deb1c) → [`008deb40`](#insn-008deb40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deb24`](#insn-008deb24) → `00c65f28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`008deb2c`](#insn-008deb2c) → `00c85168`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`008deb34`](#insn-008deb34) → [`00c586e0`](../00c58/00c586e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c586e0` · 推定シンボル `None` · 推定型 `None`
- [`008deb3c`](#insn-008deb3c) → [`008deb44`](#insn-008deb44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deb48`](#insn-008deb48) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`008deb5c`](#insn-008deb5c) → [`00489f8c`](../00489/00489f8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00489f8c` · 推定シンボル `None` · 推定型 `None`
- [`008deb6c`](#insn-008deb6c) → [`008deb88`](#insn-008deb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deb70`](#insn-008deb70) → `00ca5038`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008deb74`](#insn-008deb74) → [`008df414`](#insn-008df414) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deb78`](#insn-008deb78) → `00ca5030`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008deb7c`](#insn-008deb7c) → [`008deb88`](#insn-008deb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deb80`](#insn-008deb80) → [`00498844`](../00498/00498844.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00498844` · 推定シンボル `None` · 推定型 `None`
- [`008deb84`](#insn-008deb84) → [`008def30`](#insn-008def30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008deba0`](#insn-008deba0) → [`00467ba0`](../00467/00467ba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ba0` · 推定シンボル `None` · 推定型 `None`
- [`008debac`](#insn-008debac) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`008debb4`](#insn-008debb4) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008debb8`](#insn-008debb8) → [`0046cac4`](../0046c/0046cac4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046cac4` · 推定シンボル `None` · 推定型 `None`
- [`008debd8`](#insn-008debd8) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008debf0`](#insn-008debf0) → [`00467ba0`](../00467/00467ba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ba0` · 推定シンボル `None` · 推定型 `None`
- [`008debf4`](#insn-008debf4) → `00333f9c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008debfc`](#insn-008debfc) → [`0046d9ec`](../0046d/0046d9ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d9ec` · 推定シンボル `None` · 推定型 `None`
- [`008dec18`](#insn-008dec18) → [`00468c1c`](../00468/00468c1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468c1c` · 推定シンボル `None` · 推定型 `None`
- [`008dec24`](#insn-008dec24) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`008dec44`](#insn-008dec44) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008dec50`](#insn-008dec50) → [`00468c1c`](../00468/00468c1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468c1c` · 推定シンボル `None` · 推定型 `None`
- [`008dec68`](#insn-008dec68) → [`00467ba0`](../00467/00467ba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ba0` · 推定シンボル `None` · 推定型 `None`
- [`008dec74`](#insn-008dec74) → [`008dda58`](../008dd/008dda58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008dda58` · 推定シンボル `None` · 推定型 `None`
- [`008dec80`](#insn-008dec80) → [`00468ca0`](../00468/00468ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468ca0` · 推定シンボル `None` · 推定型 `None`
- [`008dec94`](#insn-008dec94) → [`00861508`](../00861/00861508.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00861508` · 推定シンボル `None` · 推定型 `None`
- [`008deca0`](#insn-008deca0) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`008decc0`](#insn-008decc0) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008decd8`](#insn-008decd8) → [`00467ba0`](../00467/00467ba0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ba0` · 推定シンボル `None` · 推定型 `None`
- [`008dece4`](#insn-008dece4) → [`00468c1c`](../00468/00468c1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468c1c` · 推定シンボル `None` · 推定型 `None`
- [`008decf4`](#insn-008decf4) → [`008ded40`](#insn-008ded40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008decfc`](#insn-008decfc) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008ded08`](#insn-008ded08) → `00333f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008ded18`](#insn-008ded18) → [`0046d9b4`](../0046d/0046d9b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d9b4` · 推定シンボル `None` · 推定型 `None`
- [`008ded3c`](#insn-008ded3c) → [`00468fc8`](../00468/00468fc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc8` · 推定シンボル `None` · 推定型 `None`
- [`008ded48`](#insn-008ded48) → [`00468ca0`](../00468/00468ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468ca0` · 推定シンボル `None` · 推定型 `None`
- [`008ded54`](#insn-008ded54) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008ded60`](#insn-008ded60) → `00335f78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008ded6c`](#insn-008ded6c) → [`008dedc4`](#insn-008dedc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008ded78`](#insn-008ded78) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`008ded84`](#insn-008ded84) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`008ded90`](#insn-008ded90) → `00333f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008deda0`](#insn-008deda0) → [`0046d9b4`](../0046d/0046d9b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d9b4` · 推定シンボル `None` · 推定型 `None`
- [`008dedc0`](#insn-008dedc0) → [`00468fc8`](../00468/00468fc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc8` · 推定シンボル `None` · 推定型 `None`
- [`008dedcc`](#insn-008dedcc) → [`00468ca0`](../00468/00468ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468ca0` · 推定シンボル `None` · 推定型 `None`
- [`008dedd8`](#insn-008dedd8) → [`00468c1c`](../00468/00468c1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468c1c` · 推定シンボル `None` · 推定型 `None`
- [`008deddc`](#insn-008deddc) → `00334174`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008dede4`](#insn-008dede4) → [`008dee04`](#insn-008dee04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dee00`](#insn-008dee00) → [`00468fc8`](../00468/00468fc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc8` · 推定シンボル `None` · 推定型 `None`
- [`008dee04`](#insn-008dee04) → `00332a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008dee08`](#insn-008dee08) → [`008dee8c`](#insn-008dee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dee0c`](#insn-008dee0c) → `00332a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008dee10`](#insn-008dee10) → [`008dee8c`](#insn-008dee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dee14`](#insn-008dee14) → `00332a2d`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008dee18`](#insn-008dee18) → [`008dee8c`](#insn-008dee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dee1c`](#insn-008dee1c) → `00332a29`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008dee20`](#insn-008dee20) → [`008dee8c`](#insn-008dee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dee24`](#insn-008dee24) → `00332a31`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008dee28`](#insn-008dee28) → [`008dee8c`](#insn-008dee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dee2c`](#insn-008dee2c) → `00332a26`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008dee30`](#insn-008dee30) → [`008dee8c`](#insn-008dee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dee34`](#insn-008dee34) → `00332060`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008dee38`](#insn-008dee38) → [`008dee8c`](#insn-008dee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dee3c`](#insn-008dee3c) → `00332a2e`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008dee40`](#insn-008dee40) → [`008dee8c`](#insn-008dee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008dee44`](#insn-008dee44) → `00333f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008dee88`](#insn-008dee88) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008deea0`](#insn-008deea0) → [`00468fc8`](../00468/00468fc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc8` · 推定シンボル `None` · 推定型 `None`
- [`008deeb8`](#insn-008deeb8) → [`00468fc8`](../00468/00468fc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc8` · 推定シンボル `None` · 推定型 `None`
- [`008deec4`](#insn-008deec4) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`008deed8`](#insn-008deed8) → [`00b3bf30`](../00b3b/00b3bf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3bf30` · 推定シンボル `None` · 推定型 `None`
- [`008def0c`](#insn-008def0c) → [`0046af4c`](../0046a/0046af4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046af4c` · 推定シンボル `None` · 推定型 `None`
- [`008def2c`](#insn-008def2c) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008def40`](#insn-008def40) → [`00acae1c`](../00aca/00acae1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acae1c` · 推定シンボル `None` · 推定型 `None`
- [`008def44`](#insn-008def44) → `00332a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008def48`](#insn-008def48) → [`008def5c`](#insn-008def5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008def4c`](#insn-008def4c) → `00332a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008def50`](#insn-008def50) → [`008def5c`](#insn-008def5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008def54`](#insn-008def54) → `00332a31`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008def58`](#insn-008def58) → [`008defc4`](#insn-008defc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008def6c`](#insn-008def6c) → [`00861508`](../00861/00861508.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00861508` · 推定シンボル `None` · 推定型 `None`
- [`008def78`](#insn-008def78) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`008def98`](#insn-008def98) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008def9c`](#insn-008def9c) → `00334174`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008defa4`](#insn-008defa4) → [`008defc4`](#insn-008defc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008defc0`](#insn-008defc0) → [`00468fc8`](../00468/00468fc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc8` · 推定シンボル `None` · 推定型 `None`
- [`008defcc`](#insn-008defcc) → [`00468ca0`](../00468/00468ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468ca0` · 推定シンボル `None` · 推定型 `None`
- [`008defd8`](#insn-008defd8) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`008deff8`](#insn-008deff8) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008df004`](#insn-008df004) → [`00468ca0`](../00468/00468ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468ca0` · 推定シンボル `None` · 推定型 `None`
- [`008df00c`](#insn-008df00c) → `00333dc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df014`](#insn-008df014) → `00c9b578`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008df020`](#insn-008df020) → `00333ccc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df020`](#insn-008df020) → `00333cd0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df024`](#insn-008df024) → `00ca4554`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df028`](#insn-008df028) → `00333cd4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df028`](#insn-008df028) → `00333cd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df048`](#insn-008df048) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008df04c`](#insn-008df04c) → `00333dc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df058`](#insn-008df058) → `00333ccc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df058`](#insn-008df058) → `00333cd0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df05c`](#insn-008df05c) → `00ca4554`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df088`](#insn-008df088) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008df08c`](#insn-008df08c) → `00332a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df090`](#insn-008df090) → [`008df0d4`](#insn-008df0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df094`](#insn-008df094) → `00332a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df098`](#insn-008df098) → [`008df0d4`](#insn-008df0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df09c`](#insn-008df09c) → `00332a2d`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df0a0`](#insn-008df0a0) → [`008df0c4`](#insn-008df0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df0a4`](#insn-008df0a4) → `00332a29`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df0a8`](#insn-008df0a8) → [`008df0c4`](#insn-008df0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df0ac`](#insn-008df0ac) → `00332a31`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df0b0`](#insn-008df0b0) → [`008df0c4`](#insn-008df0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df0b4`](#insn-008df0b4) → `00332a26`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df0b8`](#insn-008df0b8) → [`008df0c4`](#insn-008df0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df0bc`](#insn-008df0bc) → `00332060`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df0c0`](#insn-008df0c0) → [`008df354`](#insn-008df354) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df0c4`](#insn-008df0c4) → `00332a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df0c8`](#insn-008df0c8) → [`008df0d4`](#insn-008df0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df0cc`](#insn-008df0cc) → `00332a31`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df0d0`](#insn-008df0d0) → [`008df178`](#insn-008df178) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df0e8`](#insn-008df0e8) → [`00468fc8`](../00468/00468fc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc8` · 推定シンボル `None` · 推定型 `None`
- [`008df100`](#insn-008df100) → [`00468fc8`](../00468/00468fc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc8` · 推定シンボル `None` · 推定型 `None`
- [`008df10c`](#insn-008df10c) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`008df120`](#insn-008df120) → [`00b3bf30`](../00b3b/00b3bf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3bf30` · 推定シンボル `None` · 推定型 `None`
- [`008df154`](#insn-008df154) → [`0046af4c`](../0046a/0046af4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046af4c` · 推定シンボル `None` · 推定型 `None`
- [`008df174`](#insn-008df174) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008df180`](#insn-008df180) → [`00468ca0`](../00468/00468ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468ca0` · 推定シンボル `None` · 推定型 `None`
- [`008df198`](#insn-008df198) → [`00468fc8`](../00468/00468fc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468fc8` · 推定シンボル `None` · 推定型 `None`
- [`008df1a4`](#insn-008df1a4) → [`00468ca0`](../00468/00468ca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468ca0` · 推定シンボル `None` · 推定型 `None`
- [`008df1c0`](#insn-008df1c0) → [`0077bb04`](../0077b/0077bb04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0077bb04` · 推定シンボル `None` · 推定型 `None`
- [`008df1cc`](#insn-008df1cc) → [`0046ca04`](../0046c/0046ca04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca04` · 推定シンボル `None` · 推定型 `None`
- [`008df1e0`](#insn-008df1e0) → [`00b3bf30`](../00b3b/00b3bf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3bf30` · 推定シンボル `None` · 推定型 `None`
- [`008df218`](#insn-008df218) → [`0046af4c`](../0046a/0046af4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046af4c` · 推定シンボル `None` · 推定型 `None`
- [`008df21c`](#insn-008df21c) → `00333dc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df228`](#insn-008df228) → `00333ccc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df228`](#insn-008df228) → `00333cd0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df22c`](#insn-008df22c) → `00ca4554`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df234`](#insn-008df234) → `00333cd4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df234`](#insn-008df234) → `00333cd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df254`](#insn-008df254) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008df258`](#insn-008df258) → `00333dc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df264`](#insn-008df264) → `00333ccc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df264`](#insn-008df264) → `00333cd0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df268`](#insn-008df268) → `00ca4554`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df294`](#insn-008df294) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008df298`](#insn-008df298) → `00332a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df29c`](#insn-008df29c) → [`008df320`](#insn-008df320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df2a0`](#insn-008df2a0) → `00332a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df2a4`](#insn-008df2a4) → [`008df320`](#insn-008df320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df2a8`](#insn-008df2a8) → `00332a2d`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df2ac`](#insn-008df2ac) → [`008df320`](#insn-008df320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df2b0`](#insn-008df2b0) → `00332a29`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df2b4`](#insn-008df2b4) → [`008df320`](#insn-008df320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df2b8`](#insn-008df2b8) → `00332a31`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df2bc`](#insn-008df2bc) → [`008df320`](#insn-008df320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df2c0`](#insn-008df2c0) → `00332a26`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df2c4`](#insn-008df2c4) → [`008df320`](#insn-008df320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df2c8`](#insn-008df2c8) → `00332060`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df2cc`](#insn-008df2cc) → [`008df320`](#insn-008df320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df2d0`](#insn-008df2d0) → `00332a2e`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df2d4`](#insn-008df2d4) → [`008df320`](#insn-008df320) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df2d8`](#insn-008df2d8) → `00333f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df31c`](#insn-008df31c) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008df324`](#insn-008df324) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df32c`](#insn-008df32c) → [`008df410`](#insn-008df410) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df330`](#insn-008df330) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df334`](#insn-008df334) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df338`](#insn-008df338) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df33c`](#insn-008df33c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df340`](#insn-008df340) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df344`](#insn-008df344) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df348`](#insn-008df348) → `Stack[-0x58]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df354`](#insn-008df354) → `00332a2e`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df358`](#insn-008df358) → [`008df0c4`](#insn-008df0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df35c`](#insn-008df35c) → `00333f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df3a0`](#insn-008df3a0) → [`00469c44`](../00469/00469c44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c44` · 推定シンボル `None` · 推定型 `None`
- [`008df3a4`](#insn-008df3a4) → `00332a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df3a8`](#insn-008df3a8) → `00332a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`008df3b0`](#insn-008df3b0) → [`008df0cc`](#insn-008df0cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df3b4`](#insn-008df3b4) → [`008df0d4`](#insn-008df0d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df3bc`](#insn-008df3bc) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008df3c0`](#insn-008df3c0) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`008df3c4`](#insn-008df3c4) → [`008deaf4`](#insn-008deaf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df3cc`](#insn-008df3cc) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df3d4`](#insn-008df3d4) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`008df3e0`](#insn-008df3e0) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008df3e4`](#insn-008df3e4) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df3e8`](#insn-008df3e8) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df3e8`](#insn-008df3e8) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df3f0`](#insn-008df3f0) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df3f0`](#insn-008df3f0) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df3f4`](#insn-008df3f4) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df3f8`](#insn-008df3f8) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df3f8`](#insn-008df3f8) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df3f8`](#insn-008df3f8) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df3fc`](#insn-008df3fc) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`008df404`](#insn-008df404) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008df408`](#insn-008df408) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`008df40c`](#insn-008df40c) → [`008deaf4`](#insn-008deaf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df410`](#insn-008df410) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`
- [`008df418`](#insn-008df418) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008df41c`](#insn-008df41c) → [`00c57f20`](../00c57/00c57f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f20` · 推定シンボル `None` · 推定型 `None`
- [`008df420`](#insn-008df420) → [`008deb78`](#insn-008deb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008df428`](#insn-008df428) → `00ca5000`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df430`](#insn-008df430) → [`0047edf4`](../0047e/0047edf4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edf4` · 推定シンボル `None` · 推定型 `None`
- [`008df43c`](#insn-008df43c) → `00c63060`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`008df440`](#insn-008df440) → `00ca5008`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df444`](#insn-008df444) → `00ca5000`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df444`](#insn-008df444) → `00ca5008`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df44c`](#insn-008df44c) → `00ca5028`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df44c`](#insn-008df44c) → `00ca5030`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df450`](#insn-008df450) → `00ca5020`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df454`](#insn-008df454) → `00ca5010`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df454`](#insn-008df454) → `00ca5018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df454`](#insn-008df454) → `00ca5020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`008df458`](#insn-008df458) → [`00c57f00`](../00c57/00c57f00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f00` · 推定シンボル `None` · 推定型 `None`
- [`008df460`](#insn-008df460) → `00ca5038`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`008df464`](#insn-008df464) → [`00c57f40`](../00c57/00c57f40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f40` · 推定シンボル `None` · 推定型 `None`
- [`008df468`](#insn-008df468) → [`008deb78`](#insn-008deb78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008deab0`](#insn-008deab0)

~~~json
{
  "source": "008deab0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deab4`](#insn-008deab4)

~~~json
{
  "source": "008deab4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deab8`](#insn-008deab8)

~~~json
{
  "source": "008deab8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deabc`](#insn-008deabc)

~~~json
{
  "source": "008deabc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deac0`](#insn-008deac0)

~~~json
{
  "source": "008deac0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deac4`](#insn-008deac4)

~~~json
{
  "source": "008deac4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deac8`](#insn-008deac8)

~~~json
{
  "source": "008deac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deae8`](#insn-008deae8)

~~~json
{
  "source": "008deae8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deaec`](#insn-008deaec)

~~~json
{
  "source": "008deaec",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008deaf0`](#insn-008deaf0)

~~~json
{
  "source": "008deaf0",
  "target": "008df3b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deaf8`](#insn-008deaf8)

~~~json
{
  "source": "008deaf8",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008deafc`](#insn-008deafc)

~~~json
{
  "source": "008deafc",
  "target": "008deb04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deb00`](#insn-008deb00)

~~~json
{
  "source": "008deb00",
  "target": "00498210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008deb0c`](#insn-008deb0c)

~~~json
{
  "source": "008deb0c",
  "target": "00ca4a78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4a78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008deb1c`](#insn-008deb1c)

~~~json
{
  "source": "008deb1c",
  "target": "008deb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deb24`](#insn-008deb24)

~~~json
{
  "source": "008deb24",
  "target": "00c65f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65f28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008deb2c`](#insn-008deb2c)

~~~json
{
  "source": "008deb2c",
  "target": "00c85168",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c85168",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008deb34`](#insn-008deb34)

~~~json
{
  "source": "008deb34",
  "target": "00c586e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008deb3c`](#insn-008deb3c)

~~~json
{
  "source": "008deb3c",
  "target": "008deb44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deb48`](#insn-008deb48)

~~~json
{
  "source": "008deb48",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008deb5c`](#insn-008deb5c)

~~~json
{
  "source": "008deb5c",
  "target": "00489f8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008deb6c`](#insn-008deb6c)

~~~json
{
  "source": "008deb6c",
  "target": "008deb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deb70`](#insn-008deb70)

~~~json
{
  "source": "008deb70",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008deb74`](#insn-008deb74)

~~~json
{
  "source": "008deb74",
  "target": "008df414",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deb78`](#insn-008deb78)

~~~json
{
  "source": "008deb78",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008deb7c`](#insn-008deb7c)

~~~json
{
  "source": "008deb7c",
  "target": "008deb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deb80`](#insn-008deb80)

~~~json
{
  "source": "008deb80",
  "target": "00498844",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008deb84`](#insn-008deb84)

~~~json
{
  "source": "008deb84",
  "target": "008def30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008deba0`](#insn-008deba0)

~~~json
{
  "source": "008deba0",
  "target": "00467ba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008debac`](#insn-008debac)

~~~json
{
  "source": "008debac",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008debb4`](#insn-008debb4)

~~~json
{
  "source": "008debb4",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008debb8`](#insn-008debb8)

~~~json
{
  "source": "008debb8",
  "target": "0046cac4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008debd8`](#insn-008debd8)

~~~json
{
  "source": "008debd8",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008debf0`](#insn-008debf0)

~~~json
{
  "source": "008debf0",
  "target": "00467ba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008debf4`](#insn-008debf4)

~~~json
{
  "source": "008debf4",
  "target": "00333f9c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "88a76c0014261100",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008debfc`](#insn-008debfc)

~~~json
{
  "source": "008debfc",
  "target": "0046d9ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dec18`](#insn-008dec18)

~~~json
{
  "source": "008dec18",
  "target": "00468c1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dec24`](#insn-008dec24)

~~~json
{
  "source": "008dec24",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dec44`](#insn-008dec44)

~~~json
{
  "source": "008dec44",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dec50`](#insn-008dec50)

~~~json
{
  "source": "008dec50",
  "target": "00468c1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dec68`](#insn-008dec68)

~~~json
{
  "source": "008dec68",
  "target": "00467ba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dec74`](#insn-008dec74)

~~~json
{
  "source": "008dec74",
  "target": "008dda58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dec80`](#insn-008dec80)

~~~json
{
  "source": "008dec80",
  "target": "00468ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dec94`](#insn-008dec94)

~~~json
{
  "source": "008dec94",
  "target": "00861508",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008deca0`](#insn-008deca0)

~~~json
{
  "source": "008deca0",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008decc0`](#insn-008decc0)

~~~json
{
  "source": "008decc0",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008decd8`](#insn-008decd8)

~~~json
{
  "source": "008decd8",
  "target": "00467ba0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dece4`](#insn-008dece4)

~~~json
{
  "source": "008dece4",
  "target": "00468c1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008decf4`](#insn-008decf4)

~~~json
{
  "source": "008decf4",
  "target": "008ded40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008decfc`](#insn-008decfc)

~~~json
{
  "source": "008decfc",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ded08`](#insn-008ded08)

~~~json
{
  "source": "008ded08",
  "target": "00333f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "88a76c0014261100",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008ded18`](#insn-008ded18)

~~~json
{
  "source": "008ded18",
  "target": "0046d9b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ded3c`](#insn-008ded3c)

~~~json
{
  "source": "008ded3c",
  "target": "00468fc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ded48`](#insn-008ded48)

~~~json
{
  "source": "008ded48",
  "target": "00468ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ded54`](#insn-008ded54)

~~~json
{
  "source": "008ded54",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ded60`](#insn-008ded60)

~~~json
{
  "source": "008ded60",
  "target": "00335f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335f78",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "306f7500bcfe0900",
  "capture_start": "00335f78",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008ded6c`](#insn-008ded6c)

~~~json
{
  "source": "008ded6c",
  "target": "008dedc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008ded78`](#insn-008ded78)

~~~json
{
  "source": "008ded78",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ded84`](#insn-008ded84)

~~~json
{
  "source": "008ded84",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008ded90`](#insn-008ded90)

~~~json
{
  "source": "008ded90",
  "target": "00333f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "88a76c0014261100",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008deda0`](#insn-008deda0)

~~~json
{
  "source": "008deda0",
  "target": "0046d9b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dedc0`](#insn-008dedc0)

~~~json
{
  "source": "008dedc0",
  "target": "00468fc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dedcc`](#insn-008dedcc)

~~~json
{
  "source": "008dedcc",
  "target": "00468ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dedd8`](#insn-008dedd8)

~~~json
{
  "source": "008dedd8",
  "target": "00468c1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008deddc`](#insn-008deddc)

~~~json
{
  "source": "008deddc",
  "target": "00334174",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "04246d00f8940900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008dede4`](#insn-008dede4)

~~~json
{
  "source": "008dede4",
  "target": "008dee04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dee00`](#insn-008dee00)

~~~json
{
  "source": "008dee00",
  "target": "00468fc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008dee04`](#insn-008dee04)

~~~json
{
  "source": "008dee04",
  "target": "00332a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008dee08`](#insn-008dee08)

~~~json
{
  "source": "008dee08",
  "target": "008dee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dee0c`](#insn-008dee0c)

~~~json
{
  "source": "008dee0c",
  "target": "00332a25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008dee10`](#insn-008dee10)

~~~json
{
  "source": "008dee10",
  "target": "008dee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dee14`](#insn-008dee14)

~~~json
{
  "source": "008dee14",
  "target": "00332a2d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cf968001c470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008dee18`](#insn-008dee18)

~~~json
{
  "source": "008dee18",
  "target": "008dee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dee1c`](#insn-008dee1c)

~~~json
{
  "source": "008dee1c",
  "target": "00332a29",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 1,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cf968001c470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008dee20`](#insn-008dee20)

~~~json
{
  "source": "008dee20",
  "target": "008dee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dee24`](#insn-008dee24)

~~~json
{
  "source": "008dee24",
  "target": "00332a31",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a30",
  "offset": 1,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "94f9680030470900",
  "capture_start": "00332a30",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008dee28`](#insn-008dee28)

~~~json
{
  "source": "008dee28",
  "target": "008dee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dee2c`](#insn-008dee2c)

~~~json
{
  "source": "008dee2c",
  "target": "00332a26",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008dee30`](#insn-008dee30)

~~~json
{
  "source": "008dee30",
  "target": "008dee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dee34`](#insn-008dee34)

~~~json
{
  "source": "008dee34",
  "target": "00332060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332060",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "54ff6100c4230900",
  "capture_start": "00332060",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008dee38`](#insn-008dee38)

~~~json
{
  "source": "008dee38",
  "target": "008dee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dee3c`](#insn-008dee3c)

~~~json
{
  "source": "008dee3c",
  "target": "00332a2e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cf968001c470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008dee40`](#insn-008dee40)

~~~json
{
  "source": "008dee40",
  "target": "008dee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008dee44`](#insn-008dee44)

~~~json
{
  "source": "008dee44",
  "target": "00333f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "88a76c0014261100",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008dee88`](#insn-008dee88)

~~~json
{
  "source": "008dee88",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008deea0`](#insn-008deea0)

~~~json
{
  "source": "008deea0",
  "target": "00468fc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008deeb8`](#insn-008deeb8)

~~~json
{
  "source": "008deeb8",
  "target": "00468fc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008deec4`](#insn-008deec4)

~~~json
{
  "source": "008deec4",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008deed8`](#insn-008deed8)

~~~json
{
  "source": "008deed8",
  "target": "00b3bf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008def0c`](#insn-008def0c)

~~~json
{
  "source": "008def0c",
  "target": "0046af4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008def2c`](#insn-008def2c)

~~~json
{
  "source": "008def2c",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008def40`](#insn-008def40)

~~~json
{
  "source": "008def40",
  "target": "00acae1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008def44`](#insn-008def44)

~~~json
{
  "source": "008def44",
  "target": "00332a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008def48`](#insn-008def48)

~~~json
{
  "source": "008def48",
  "target": "008def5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008def4c`](#insn-008def4c)

~~~json
{
  "source": "008def4c",
  "target": "00332a25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008def50`](#insn-008def50)

~~~json
{
  "source": "008def50",
  "target": "008def5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008def54`](#insn-008def54)

~~~json
{
  "source": "008def54",
  "target": "00332a31",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a30",
  "offset": 1,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "94f9680030470900",
  "capture_start": "00332a30",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008def58`](#insn-008def58)

~~~json
{
  "source": "008def58",
  "target": "008defc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008def6c`](#insn-008def6c)

~~~json
{
  "source": "008def6c",
  "target": "00861508",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008def78`](#insn-008def78)

~~~json
{
  "source": "008def78",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008def98`](#insn-008def98)

~~~json
{
  "source": "008def98",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008def9c`](#insn-008def9c)

~~~json
{
  "source": "008def9c",
  "target": "00334174",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "04246d00f8940900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008defa4`](#insn-008defa4)

~~~json
{
  "source": "008defa4",
  "target": "008defc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008defc0`](#insn-008defc0)

~~~json
{
  "source": "008defc0",
  "target": "00468fc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008defcc`](#insn-008defcc)

~~~json
{
  "source": "008defcc",
  "target": "00468ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008defd8`](#insn-008defd8)

~~~json
{
  "source": "008defd8",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008deff8`](#insn-008deff8)

~~~json
{
  "source": "008deff8",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df004`](#insn-008df004)

~~~json
{
  "source": "008df004",
  "target": "00468ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df00c`](#insn-008df00c)

~~~json
{
  "source": "008df00c",
  "target": "00333dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333dc0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "18c26b00dc201100",
  "capture_start": "00333dc0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df014`](#insn-008df014)

~~~json
{
  "source": "008df014",
  "target": "00c9b578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b578",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008df020`](#insn-008df020)

~~~json
{
  "source": "008df020",
  "target": "00333ccc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cc8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6c1f6b003c1e1100",
  "capture_start": "00333cc8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df020`](#insn-008df020)

~~~json
{
  "source": "008df020",
  "target": "00333cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "34366b00a0800900",
  "capture_start": "00333cd0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df024`](#insn-008df024)

~~~json
{
  "source": "008df024",
  "target": "00ca4554",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df028`](#insn-008df028)

~~~json
{
  "source": "008df028",
  "target": "00333cd4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd0",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "34366b00a0800900",
  "capture_start": "00333cd0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df028`](#insn-008df028)

~~~json
{
  "source": "008df028",
  "target": "00333cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "74366b00c8800900",
  "capture_start": "00333cd8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df048`](#insn-008df048)

~~~json
{
  "source": "008df048",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df04c`](#insn-008df04c)

~~~json
{
  "source": "008df04c",
  "target": "00333dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333dc0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "18c26b00dc201100",
  "capture_start": "00333dc0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df058`](#insn-008df058)

~~~json
{
  "source": "008df058",
  "target": "00333ccc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cc8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6c1f6b003c1e1100",
  "capture_start": "00333cc8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df058`](#insn-008df058)

~~~json
{
  "source": "008df058",
  "target": "00333cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "34366b00a0800900",
  "capture_start": "00333cd0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df05c`](#insn-008df05c)

~~~json
{
  "source": "008df05c",
  "target": "00ca4554",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df088`](#insn-008df088)

~~~json
{
  "source": "008df088",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df08c`](#insn-008df08c)

~~~json
{
  "source": "008df08c",
  "target": "00332a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df090`](#insn-008df090)

~~~json
{
  "source": "008df090",
  "target": "008df0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df094`](#insn-008df094)

~~~json
{
  "source": "008df094",
  "target": "00332a25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df098`](#insn-008df098)

~~~json
{
  "source": "008df098",
  "target": "008df0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df09c`](#insn-008df09c)

~~~json
{
  "source": "008df09c",
  "target": "00332a2d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cf968001c470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df0a0`](#insn-008df0a0)

~~~json
{
  "source": "008df0a0",
  "target": "008df0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df0a4`](#insn-008df0a4)

~~~json
{
  "source": "008df0a4",
  "target": "00332a29",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 1,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cf968001c470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df0a8`](#insn-008df0a8)

~~~json
{
  "source": "008df0a8",
  "target": "008df0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df0ac`](#insn-008df0ac)

~~~json
{
  "source": "008df0ac",
  "target": "00332a31",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a30",
  "offset": 1,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "94f9680030470900",
  "capture_start": "00332a30",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df0b0`](#insn-008df0b0)

~~~json
{
  "source": "008df0b0",
  "target": "008df0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df0b4`](#insn-008df0b4)

~~~json
{
  "source": "008df0b4",
  "target": "00332a26",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df0b8`](#insn-008df0b8)

~~~json
{
  "source": "008df0b8",
  "target": "008df0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df0bc`](#insn-008df0bc)

~~~json
{
  "source": "008df0bc",
  "target": "00332060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332060",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "54ff6100c4230900",
  "capture_start": "00332060",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df0c0`](#insn-008df0c0)

~~~json
{
  "source": "008df0c0",
  "target": "008df354",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df0c4`](#insn-008df0c4)

~~~json
{
  "source": "008df0c4",
  "target": "00332a25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df0c8`](#insn-008df0c8)

~~~json
{
  "source": "008df0c8",
  "target": "008df0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df0cc`](#insn-008df0cc)

~~~json
{
  "source": "008df0cc",
  "target": "00332a31",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a30",
  "offset": 1,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "94f9680030470900",
  "capture_start": "00332a30",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df0d0`](#insn-008df0d0)

~~~json
{
  "source": "008df0d0",
  "target": "008df178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df0e8`](#insn-008df0e8)

~~~json
{
  "source": "008df0e8",
  "target": "00468fc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df100`](#insn-008df100)

~~~json
{
  "source": "008df100",
  "target": "00468fc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df10c`](#insn-008df10c)

~~~json
{
  "source": "008df10c",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df120`](#insn-008df120)

~~~json
{
  "source": "008df120",
  "target": "00b3bf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df154`](#insn-008df154)

~~~json
{
  "source": "008df154",
  "target": "0046af4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df174`](#insn-008df174)

~~~json
{
  "source": "008df174",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df180`](#insn-008df180)

~~~json
{
  "source": "008df180",
  "target": "00468ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df198`](#insn-008df198)

~~~json
{
  "source": "008df198",
  "target": "00468fc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df1a4`](#insn-008df1a4)

~~~json
{
  "source": "008df1a4",
  "target": "00468ca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df1c0`](#insn-008df1c0)

~~~json
{
  "source": "008df1c0",
  "target": "0077bb04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df1cc`](#insn-008df1cc)

~~~json
{
  "source": "008df1cc",
  "target": "0046ca04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df1e0`](#insn-008df1e0)

~~~json
{
  "source": "008df1e0",
  "target": "00b3bf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df218`](#insn-008df218)

~~~json
{
  "source": "008df218",
  "target": "0046af4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df21c`](#insn-008df21c)

~~~json
{
  "source": "008df21c",
  "target": "00333dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333dc0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "18c26b00dc201100",
  "capture_start": "00333dc0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df228`](#insn-008df228)

~~~json
{
  "source": "008df228",
  "target": "00333ccc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cc8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6c1f6b003c1e1100",
  "capture_start": "00333cc8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df228`](#insn-008df228)

~~~json
{
  "source": "008df228",
  "target": "00333cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "34366b00a0800900",
  "capture_start": "00333cd0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df22c`](#insn-008df22c)

~~~json
{
  "source": "008df22c",
  "target": "00ca4554",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df234`](#insn-008df234)

~~~json
{
  "source": "008df234",
  "target": "00333cd4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd0",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "34366b00a0800900",
  "capture_start": "00333cd0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df234`](#insn-008df234)

~~~json
{
  "source": "008df234",
  "target": "00333cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "74366b00c8800900",
  "capture_start": "00333cd8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df254`](#insn-008df254)

~~~json
{
  "source": "008df254",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df258`](#insn-008df258)

~~~json
{
  "source": "008df258",
  "target": "00333dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333dc0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "18c26b00dc201100",
  "capture_start": "00333dc0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df264`](#insn-008df264)

~~~json
{
  "source": "008df264",
  "target": "00333ccc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cc8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6c1f6b003c1e1100",
  "capture_start": "00333cc8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df264`](#insn-008df264)

~~~json
{
  "source": "008df264",
  "target": "00333cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "34366b00a0800900",
  "capture_start": "00333cd0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df268`](#insn-008df268)

~~~json
{
  "source": "008df268",
  "target": "00ca4554",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df294`](#insn-008df294)

~~~json
{
  "source": "008df294",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df298`](#insn-008df298)

~~~json
{
  "source": "008df298",
  "target": "00332a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df29c`](#insn-008df29c)

~~~json
{
  "source": "008df29c",
  "target": "008df320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df2a0`](#insn-008df2a0)

~~~json
{
  "source": "008df2a0",
  "target": "00332a25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df2a4`](#insn-008df2a4)

~~~json
{
  "source": "008df2a4",
  "target": "008df320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df2a8`](#insn-008df2a8)

~~~json
{
  "source": "008df2a8",
  "target": "00332a2d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cf968001c470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df2ac`](#insn-008df2ac)

~~~json
{
  "source": "008df2ac",
  "target": "008df320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df2b0`](#insn-008df2b0)

~~~json
{
  "source": "008df2b0",
  "target": "00332a29",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 1,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cf968001c470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df2b4`](#insn-008df2b4)

~~~json
{
  "source": "008df2b4",
  "target": "008df320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df2b8`](#insn-008df2b8)

~~~json
{
  "source": "008df2b8",
  "target": "00332a31",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a30",
  "offset": 1,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "94f9680030470900",
  "capture_start": "00332a30",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df2bc`](#insn-008df2bc)

~~~json
{
  "source": "008df2bc",
  "target": "008df320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df2c0`](#insn-008df2c0)

~~~json
{
  "source": "008df2c0",
  "target": "00332a26",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df2c4`](#insn-008df2c4)

~~~json
{
  "source": "008df2c4",
  "target": "008df320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df2c8`](#insn-008df2c8)

~~~json
{
  "source": "008df2c8",
  "target": "00332060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332060",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "54ff6100c4230900",
  "capture_start": "00332060",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df2cc`](#insn-008df2cc)

~~~json
{
  "source": "008df2cc",
  "target": "008df320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df2d0`](#insn-008df2d0)

~~~json
{
  "source": "008df2d0",
  "target": "00332a2e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cf968001c470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df2d4`](#insn-008df2d4)

~~~json
{
  "source": "008df2d4",
  "target": "008df320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df2d8`](#insn-008df2d8)

~~~json
{
  "source": "008df2d8",
  "target": "00333f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "88a76c0014261100",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df31c`](#insn-008df31c)

~~~json
{
  "source": "008df31c",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df324`](#insn-008df324)

~~~json
{
  "source": "008df324",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df32c`](#insn-008df32c)

~~~json
{
  "source": "008df32c",
  "target": "008df410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df330`](#insn-008df330)

~~~json
{
  "source": "008df330",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df334`](#insn-008df334)

~~~json
{
  "source": "008df334",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df338`](#insn-008df338)

~~~json
{
  "source": "008df338",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df33c`](#insn-008df33c)

~~~json
{
  "source": "008df33c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df340`](#insn-008df340)

~~~json
{
  "source": "008df340",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df344`](#insn-008df344)

~~~json
{
  "source": "008df344",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df348`](#insn-008df348)

~~~json
{
  "source": "008df348",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df354`](#insn-008df354)

~~~json
{
  "source": "008df354",
  "target": "00332a2e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cf968001c470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df358`](#insn-008df358)

~~~json
{
  "source": "008df358",
  "target": "008df0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df35c`](#insn-008df35c)

~~~json
{
  "source": "008df35c",
  "target": "00333f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "88a76c0014261100",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df3a0`](#insn-008df3a0)

~~~json
{
  "source": "008df3a0",
  "target": "00469c44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df3a4`](#insn-008df3a4)

~~~json
{
  "source": "008df3a4",
  "target": "00332a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df3a8`](#insn-008df3a8)

~~~json
{
  "source": "008df3a8",
  "target": "00332a25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78f9680008470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`008df3b0`](#insn-008df3b0)

~~~json
{
  "source": "008df3b0",
  "target": "008df0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df3b4`](#insn-008df3b4)

~~~json
{
  "source": "008df3b4",
  "target": "008df0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df3bc`](#insn-008df3bc)

~~~json
{
  "source": "008df3bc",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df3c0`](#insn-008df3c0)

~~~json
{
  "source": "008df3c0",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df3c4`](#insn-008df3c4)

~~~json
{
  "source": "008df3c4",
  "target": "008deaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df3cc`](#insn-008df3cc)

~~~json
{
  "source": "008df3cc",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df3d4`](#insn-008df3d4)

~~~json
{
  "source": "008df3d4",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df3e0`](#insn-008df3e0)

~~~json
{
  "source": "008df3e0",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008df3e4`](#insn-008df3e4)

~~~json
{
  "source": "008df3e4",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df3e8`](#insn-008df3e8)

~~~json
{
  "source": "008df3e8",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df3e8`](#insn-008df3e8)

~~~json
{
  "source": "008df3e8",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df3f0`](#insn-008df3f0)

~~~json
{
  "source": "008df3f0",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df3f0`](#insn-008df3f0)

~~~json
{
  "source": "008df3f0",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df3f4`](#insn-008df3f4)

~~~json
{
  "source": "008df3f4",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df3f8`](#insn-008df3f8)

~~~json
{
  "source": "008df3f8",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df3f8`](#insn-008df3f8)

~~~json
{
  "source": "008df3f8",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df3f8`](#insn-008df3f8)

~~~json
{
  "source": "008df3f8",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df3fc`](#insn-008df3fc)

~~~json
{
  "source": "008df3fc",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df404`](#insn-008df404)

~~~json
{
  "source": "008df404",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df408`](#insn-008df408)

~~~json
{
  "source": "008df408",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df40c`](#insn-008df40c)

~~~json
{
  "source": "008df40c",
  "target": "008deaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df410`](#insn-008df410)

~~~json
{
  "source": "008df410",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df418`](#insn-008df418)

~~~json
{
  "source": "008df418",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df41c`](#insn-008df41c)

~~~json
{
  "source": "008df41c",
  "target": "00c57f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df420`](#insn-008df420)

~~~json
{
  "source": "008df420",
  "target": "008deb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008df428`](#insn-008df428)

~~~json
{
  "source": "008df428",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df430`](#insn-008df430)

~~~json
{
  "source": "008df430",
  "target": "0047edf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df43c`](#insn-008df43c)

~~~json
{
  "source": "008df43c",
  "target": "00c63060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c63060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`008df440`](#insn-008df440)

~~~json
{
  "source": "008df440",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df444`](#insn-008df444)

~~~json
{
  "source": "008df444",
  "target": "00ca5000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5000",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df444`](#insn-008df444)

~~~json
{
  "source": "008df444",
  "target": "00ca5008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5008",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df44c`](#insn-008df44c)

~~~json
{
  "source": "008df44c",
  "target": "00ca5028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5028",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df44c`](#insn-008df44c)

~~~json
{
  "source": "008df44c",
  "target": "00ca5030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df450`](#insn-008df450)

~~~json
{
  "source": "008df450",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df454`](#insn-008df454)

~~~json
{
  "source": "008df454",
  "target": "00ca5010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5010",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df454`](#insn-008df454)

~~~json
{
  "source": "008df454",
  "target": "00ca5018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df454`](#insn-008df454)

~~~json
{
  "source": "008df454",
  "target": "00ca5020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5020",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df458`](#insn-008df458)

~~~json
{
  "source": "008df458",
  "target": "00c57f00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df460`](#insn-008df460)

~~~json
{
  "source": "008df460",
  "target": "00ca5038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca5038",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`008df464`](#insn-008df464)

~~~json
{
  "source": "008df464",
  "target": "00c57f40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008df468`](#insn-008df468)

~~~json
{
  "source": "008df468",
  "target": "008deb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
