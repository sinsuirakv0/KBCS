# 008bbccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `008bad20`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/008ba/008bad20.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0052.md#compare-75454af7c723385c0c428e900509d6a5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "008bbccc",
  "name": "FUN_008bbccc",
  "size": 1000,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3eda8dbfb6cb7deeefb4ec64b8de815084d8aaa9cbdb1e6c0051f03174fa1430",
  "source_text_sha256": "3eda8dbfb6cb7deeefb4ec64b8de815084d8aaa9cbdb1e6c0051f03174fa1430",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "008bbccc",
        "008bc05b"
      ],
      [
        "008bc094",
        "008bc0c7"
      ],
      [
        "008bc0cc",
        "008bc0ef"
      ]
    ],
    "bytes_sha256": "5766dca7b582beb30716acb5bc5f381d951a4e45a3622fc72909c382c8731e19",
    "instruction_count": 250,
    "instruction_bytes": 1000,
    "body_bytes": 1000,
    "indirect": 7,
    "unresolved": 7
  }
}
~~~

## 呼び出し元

- [005d9374](../005d9/005d9374.md)
- [005db878](../005db/005db878.md)
- [005dbcb0](../005db/005dbcb0.md)
- [00606ed4](../00606/00606ed4.md)
- [0060e4b4](../0060e/0060e4b4.md)
- [006107ac](../00610/006107ac.md)
- [0061491c](../00614/0061491c.md)
- [00616d40](../00616/00616d40.md)
- [006268b4](../00626/006268b4.md)
- [00634e54](../00634/00634e54.md)
- [00670364](../00670/00670364.md)
- [0068eb5c](../0068e/0068eb5c.md)
- [0068f188](../0068f/0068f188.md)
- [0068f9e0](../0068f/0068f9e0.md)
- [006912a8](../00691/006912a8.md)
- [006ae338](../006ae/006ae338.md)
- [006db7e8](../006db/006db7e8.md)
- [006ffa48](../006ff/006ffa48.md)
- [00700f00](../00700/00700f00.md)
- [007419d8](../00741/007419d8.md)
- [0076a1b8](../0076a/0076a1b8.md)
- [00772d14](../00772/00772d14.md)
- [00782820](../00782/00782820.md)
- [00782c50](../00782/00782c50.md)
- [00798494](../00798/00798494.md)
- [007cdea8](../007cd/007cdea8.md)
- [007f3a1c](../007f3/007f3a1c.md)
- [007f4a30](../007f4/007f4a30.md)
- [007f719c](../007f7/007f719c.md)
- [007f74c0](../007f7/007f74c0.md)
- [007f783c](../007f7/007f783c.md)
- [007fb104](../007fb/007fb104.md)
- [007fb94c](../007fb/007fb94c.md)
- [007fe5ac](../007fe/007fe5ac.md)
- [008002e8](../00800/008002e8.md)
- [0080064c](../00800/0080064c.md)
- [0082891c](../00828/0082891c.md)
- [00829be0](../00829/00829be0.md)
- [008322f8](../00832/008322f8.md)
- [008330d8](../00833/008330d8.md)
- [00857e30](../00857/00857e30.md)
- [0085c434](../0085c/0085c434.md)
- [00892b70](../00892/00892b70.md)
- [00893768](../00893/00893768.md)
- [008969d4](../00896/008969d4.md)
- [0089cc90](../0089c/0089cc90.md)
- [008a5538](../008a5/008a5538.md)
- [008a5c54](../008a5/008a5c54.md)
- [008add58](../008ad/008add58.md)
- [008ae314](../008ae/008ae314.md)
- [008c6da4](../008c6/008c6da4.md)
- [008ea5c0](../008ea/008ea5c0.md)
- [008eada8](../008ea/008eada8.md)
- [008f09f4](../008f0/008f09f4.md)
- [008f6be4](../008f6/008f6be4.md)
- [008fbb90](../008fb/008fbb90.md)
- [00915e30](../00915/00915e30.md)
- [00923494](../00923/00923494.md)
- [0092a498](../0092a/0092a498.md)
- [00934790](../00934/00934790.md)
- [00935eb4](../00935/00935eb4.md)
- [0094826c](../00948/0094826c.md)
- [0098ec08](../0098e/0098ec08.md)
- [009979c0](../00997/009979c0.md)
- [009afd80](../009af/009afd80.md)
- [009b0200](../009b0/009b0200.md)
- [009bb95c](../009bb/009bb95c.md)
- [009bf07c](../009bf/009bf07c.md)
- [009c06d8](../009c0/009c06d8.md)
- [009c158c](../009c1/009c158c.md)
- [009e6260](../009e6/009e6260.md)
- [009e661c](../009e6/009e661c.md)
- [009faee0](../009fa/009faee0.md)
- [009fc44c](../009fc/009fc44c.md)
- [00a8f618](../00a8f/00a8f618.md)
- [00a9b4f0](../00a9b/00a9b4f0.md)
- [00ad1470](../00ad1/00ad1470.md)
- [00ad7fb0](../00ad7/00ad7fb0.md)
- [00aeee70](../00aee/00aeee70.md)
- [00af1198](../00af1/00af1198.md)
- [00af1908](../00af1/00af1908.md)

## 呼び出し先

- [00441220](../00441/00441220.md)
- [008524fc](../00852/008524fc.md)
- [008b9358](../008b9/008b9358.md)
- [008bbc90](../008bb/008bbc90.md)
- [008bd514](../008bd/008bd514.md)
- [00c54fec](../00c54/00c54fec.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c590a0](../00c59/00c590a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 17841 bytes

~~~c

undefined8 *
FUN_008bbccc(undefined8 *param_1,undefined8 param_2,undefined4 param_3,undefined4 param_4,
            uint param_5,long *param_6)

{
  ulong uVar1;
  long lVar2;
  undefined8 *puVar3;
  long *plVar4;
  void *pvVar5;
  undefined8 *puVar6;
  undefined8 uVar7;
  long lVar8;
  ulong uVar9;
  ulong uVar10;
  void *pvVar11;
  undefined8 *puVar12;
  undefined8 *puVar13;
  undefined8 *local_d8;
  long local_d0 [4];
  long *local_b0;
  long local_a0 [4];
  long *local_80;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  puVar3 = (undefined8 *)_Znwm(0x110);
  puVar3[1] = 0;
  *puVar3 = 0;
  puVar3[3] = 0;
  puVar3[2] = 0;
  puVar3[5] = 0;
  puVar3[4] = 0;
  puVar3[7] = 0;
  puVar3[6] = 0;
  puVar3[9] = 0;
  puVar3[8] = 0;
  puVar3[0xb] = 0;
  puVar3[10] = 0;
  puVar3[0xd] = 0;
  puVar3[0xc] = 0;
  puVar3[0xf] = 0;
  puVar3[0xe] = 0;
  puVar3[0x11] = 0;
  puVar3[0x10] = 0;
  puVar3[0x13] = 0;
  puVar3[0x12] = 0;
  puVar3[0x15] = 0;
  puVar3[0x14] = 0;
  puVar3[0x17] = 0;
  puVar3[0x16] = 0;
  puVar3[0x19] = 0;
  puVar3[0x18] = 0;
  puVar3[0x1b] = 0;
  puVar3[0x1a] = 0;
  puVar3[0x1d] = 0;
  puVar3[0x1c] = 0;
  puVar3[0x1f] = 0;
  puVar3[0x1e] = 0;
  plVar4 = (long *)param_6[4];
  puVar3[0x21] = 0;
  puVar3[0x20] = 0;
  local_d8 = puVar3;
  if (plVar4 == (long *)0x0) {
    local_b0 = (long *)0x0;
    local_80 = (long *)0x0;
  }
  else if (plVar4 == param_6) {
    local_b0 = local_d0;
    (**(code **)(*param_6 + 0x18))(param_6,local_d0);
    local_80 = (long *)0x0;
    if (local_b0 != (long *)0x0) goto LAB_008bbd9c;
  }
  else {
    local_b0 = (long *)(**(code **)(*plVar4 + 0x10))();
    if (local_b0 == (long *)0x0) {
      local_80 = (long *)0x0;
    }
    else {
LAB_008bbd9c:
      if (local_b0 == local_d0) {
                    /* catch() { ... } // from try @ 008b35f4 with catch @ 008bbf28 */
        local_80 = local_a0;
                    /* catch() { ... } // from try @ 008b2c54 with catch @ 008bbf2c */
                    /* catch() { ... } // from try @ 008b2c48 with catch @ 008bbf30 */
                    /* catch() { ... } // from try @ 008b2c30 with catch @ 008bbf34 */
                    /* catch() { ... } // from try @ 008b2bf8 with catch @ 008bbf38 */
                    /* catch() { ... } // from try @ 008b2be0 with catch @ 008bbf40 */
        (**(code **)(local_d0[0] + 0x18))(local_d0,local_a0);
                    /* catch() { ... } // from try @ 008b4e04 with catch @ 008bbf44 */
      }
      else {
        local_80 = (long *)(**(code **)(*local_b0 + 0x10))();
      }
    }
  }
                    /* catch() { ... } // from try @ 008ba068 with catch @ 008bbddc */
  FUN_008b9358(puVar3,1,param_2,param_3,param_4,param_5,local_a0,0);
                    /* catch() { ... } // from try @ 008ba058 with catch @ 008bbde0 */
                    /* catch() { ... } // from try @ 008ba044 with catch @ 008bbde8 */
  if (local_80 == local_a0) {
    lVar8 = 0x20;
                    /* catch() { ... } // from try @ 008b9fcc with catch @ 008bbdfc */
    plVar4 = local_a0;
LAB_008bbe00:
                    /* catch() { ... } // from try @ 008b9fc8 with catch @ 008bbe00 */
                    /* catch() { ... } // from try @ 008b9f78 with catch @ 008bbe04 */
                    /* catch() { ... } // from try @ 008b9f68 with catch @ 008bbe08 */
    (**(code **)(*plVar4 + lVar8))();
  }
  else {
                    /* catch() { ... } // from try @ 008ba040 with catch @ 008bbdec */
    if (local_80 != (long *)0x0) {
                    /* catch() { ... } // from try @ 008b9ff0 with catch @ 008bbdf0 */
      lVar8 = 0x28;
      plVar4 = local_80;
                    /* catch() { ... } // from try @ 008b9fe0 with catch @ 008bbdf4 */
      goto LAB_008bbe00;
    }
  }
                    /* catch() { ... } // from try @ 008b9f54 with catch @ 008bbe10 */
                    /* catch() { ... } // from try @ 008b9f50 with catch @ 008bbe14 */
                    /* catch() { ... } // from try @ 008ba1a4 with catch @ 008bbe18 */
  if (local_b0 == local_d0) {
                    /* catch() { ... } // from try @ 008b9e6c with catch @ 008bbe28 */
    lVar8 = 0x20;
    plVar4 = local_d0;
LAB_008bbe30:
                    /* catch() { ... } // from try @ 008b9e58 with catch @ 008bbe30 */
                    /* catch() { ... } // from try @ 008b9e54 with catch @ 008bbe34 */
                    /* catch() { ... } // from try @ 008b9e04 with catch @ 008bbe38 */
    (**(code **)(*plVar4 + lVar8))();
  }
  else {
                    /* catch() { ... } // from try @ 008ba16c with catch @ 008bbe1c */
    if (local_b0 != (long *)0x0) {
      lVar8 = 0x28;
      plVar4 = local_b0;
                    /* catch() { ... } // from try @ 008b9e7c with catch @ 008bbe24 */
      goto LAB_008bbe30;
    }
  }
                    /* catch() { ... } // from try @ 008b9df4 with catch @ 008bbe3c */
  puVar13 = (undefined8 *)param_1[1];
                    /* catch() { ... } // from try @ 008b9de0 with catch @ 008bbe44 */
                    /* catch() { ... } // from try @ 008b9ddc with catch @ 008bbe48 */
                    /* catch() { ... } // from try @ 008b9d8c with catch @ 008bbe4c */
  if (((param_5 >> 5 & 1) == 0) || (puVar13 == (undefined8 *)*param_1)) {
                    /* catch() { ... } // from try @ 008ba0dc with catch @ 008bbe64 */
                    /* catch() { ... } // from try @ 008b9f28 with catch @ 008bbe6c */
    if (puVar13 < (undefined8 *)param_1[2]) {
                    /* catch() { ... } // from try @ 008b9ef0 with catch @ 008bbe70 */
      local_d8 = (undefined8 *)0x0;
      puVar12 = puVar13 + 1;
      *puVar13 = puVar3;
                    /* catch() { ... } // from try @ 008b9d3c with catch @ 008bbe78 */
    }
    else {
                    /* catch() { ... } // from try @ 008b9d04 with catch @ 008bbe7c */
      pvVar11 = (void *)*param_1;
                    /* catch() { ... } // from try @ 008b5318 with catch @ 008bbe84 */
      lVar8 = (long)puVar13 - (long)pvVar11 >> 3;
                    /* catch() { ... } // from try @ 008b5208 with catch @ 008bbe88 */
      uVar1 = lVar8 + 1;
                    /* catch() { ... } // from try @ 008b50f0 with catch @ 008bbe8c */
                    /* catch() { ... } // from try @ 008b4530 with catch @ 008bbe90 */
      puVar6 = param_1;
      if (uVar1 >> 0x3d != 0) goto LAB_008bc040;
                    /* catch() { ... } // from try @ 008b4420 with catch @ 008bbe94 */
      uVar9 = (long)param_1[2] - (long)pvVar11;
                    /* catch() { ... } // from try @ 008b4308 with catch @ 008bbe98 */
                    /* catch() { ... } // from try @ 008b67e8 with catch @ 008bbe9c */
      uVar10 = (long)uVar9 >> 2;
                    /* catch() { ... } // from try @ 008b67dc with catch @ 008bbea0 */
                    /* catch() { ... } // from try @ 008b67c8 with catch @ 008bbea4 */
      if (uVar10 <= uVar1) {
        uVar10 = uVar1;
      }
                    /* catch() { ... } // from try @ 008b67b8 with catch @ 008bbea8 */
                    /* catch() { ... } // from try @ 008b67ac with catch @ 008bbeb0 */
      if (0x7ffffffffffffff7 < uVar9) {
        uVar10 = 0x1fffffffffffffff;
      }
      if (uVar10 == 0) {
                    /* catch() { ... } // from try @ 008b4df8 with catch @ 008bbf48 */
        pvVar5 = (void *)0x0;
      }
      else {
                    /* catch() { ... } // from try @ 008b672c with catch @ 008bbeb8 */
                    /* catch() { ... } // from try @ 008b6798 with catch @ 008bbebc */
        if (uVar10 >> 0x3d != 0) goto LAB_008bc028;
                    /* catch() { ... } // from try @ 008b671c with catch @ 008bbec0 */
        pvVar5 = (void *)_Znwm(uVar10 << 3);
                    /* catch() { ... } // from try @ 008b6784 with catch @ 008bbec8 */
                    /* catch() { ... } // from try @ 008b6708 with catch @ 008bbecc */
      }
                    /* catch() { ... } // from try @ 008b4de4 with catch @ 008bbf4c */
      puVar6 = (undefined8 *)((long)pvVar5 + lVar8 * 8);
                    /* catch() { ... } // from try @ 008b4db0 with catch @ 008bbf50 */
                    /* catch() { ... } // from try @ 008b4da4 with catch @ 008bbf60 */
      local_d8 = (undefined8 *)0x0;
      puVar12 = puVar6 + 1;
                    /* catch() { ... } // from try @ 008b4cc4 with catch @ 008bbf64 */
      *puVar6 = puVar3;
                    /* catch() { ... } // from try @ 008b4d90 with catch @ 008bbf68 */
      memcpy(pvVar5,pvVar11,(long)puVar13 - (long)pvVar11);
                    /* catch() { ... } // from try @ 008b4c8c with catch @ 008bbf6c */
      *param_1 = pvVar5;
      param_1[1] = puVar12;
      param_1[2] = (void *)((long)pvVar5 + uVar10 * 8);
                    /* catch() { ... } // from try @ 008b3000 with catch @ 008bbf74 */
      if (pvVar11 != (void *)0x0) {
                    /* catch() { ... } // from try @ 008b2ef0 with catch @ 008bbf78 */
                    /* catch() { ... } // from try @ 008b2dd8 with catch @ 008bbf7c */
        _ZdlPv(pvVar11);
      }
    }
                    /* catch() { ... } // from try @ 008b6a14 with catch @ 008bbf80 */
    param_1[1] = puVar12;
                    /* catch() { ... } // from try @ 008b3bd0 with catch @ 008bbf84 */
    if ((param_5 >> 6 & 1) == 0) {
                    /* catch() { ... } // from try @ 008b3bc4 with catch @ 008bbf88 */
      lVar8 = FUN_008524fc();
                    /* catch() { ... } // from try @ 008b3bb0 with catch @ 008bbf8c */
                    /* catch() { ... } // from try @ 008b3b80 with catch @ 008bbf90 */
      *(undefined1 *)(lVar8 + 0x3576) = 0;
                    /* catch() { ... } // from try @ 008b3b6c with catch @ 008bbf94 */
      lVar8 = FUN_008524fc();
                    /* catch() { ... } // from try @ 008b3a90 with catch @ 008bbf98 */
                    /* catch() { ... } // from try @ 008b3a84 with catch @ 008bbf9c */
      *(undefined1 *)(lVar8 + 0x3570) = 0;
                    /* catch() { ... } // from try @ 008b3a70 with catch @ 008bbfa0 */
      lVar8 = FUN_008524fc();
                    /* catch() { ... } // from try @ 008b3a40 with catch @ 008bbfa4 */
                    /* catch() { ... } // from try @ 008b3a2c with catch @ 008bbfa8 */
      *(undefined1 *)(lVar8 + 0x3573) = 0;
                    /* catch() { ... } // from try @ 008b6b10 with catch @ 008bbfac */
      lVar8 = FUN_008524fc();
                    /* catch() { ... } // from try @ 008b9b1c with catch @ 008bbfb0 */
                    /* catch() { ... } // from try @ 008b9710 with catch @ 008bbfb4 */
      *(undefined1 *)(lVar8 + 0x3572) = 0;
                    /* catch() { ... } // from try @ 008b96dc with catch @ 008bbfb8 */
    }
  }
  else {
                    /* catch() { ... } // from try @ 008b9d7c with catch @ 008bbe50 */
    puVar13 = (undefined8 *)param_1[4];
                    /* catch() { ... } // from try @ 008b9d68 with catch @ 008bbe58 */
    if (puVar13 < (undefined8 *)param_1[5]) {
      puVar12 = puVar13 + 1;
                    /* catch() { ... } // from try @ 008b9d64 with catch @ 008bbe5c */
      *puVar13 = puVar3;
                    /* catch() { ... } // from try @ 008ba114 with catch @ 008bbe60 */
    }
    else {
                    /* catch() { ... } // from try @ 008b677c with catch @ 008bbed0 */
                    /* catch() { ... } // from try @ 008b6700 with catch @ 008bbed4 */
      pvVar11 = (void *)param_1[3];
                    /* catch() { ... } // from try @ 008b58e4 with catch @ 008bbed8 */
                    /* catch() { ... } // from try @ 008b58d8 with catch @ 008bbedc */
      lVar8 = (long)puVar13 - (long)pvVar11 >> 3;
                    /* catch() { ... } // from try @ 008b58c4 with catch @ 008bbee0 */
      uVar1 = lVar8 + 1;
                    /* catch() { ... } // from try @ 008b5894 with catch @ 008bbee4 */
      puVar6 = param_1 + 3;
      if (uVar1 >> 0x3d != 0) {
LAB_008bc040:
                    /* catch() { ... } // from try @ 008b6120 with catch @ 008bc040 */
                    /* catch() { ... } // from try @ 008b601c with catch @ 008bc044 */
        if (*(long *)(lVar2 + 0x28) != local_68) goto LAB_008bc0ec;
        uVar7 = FUN_008bd514(puVar6);
                    /* catch() { ... } // from try @ 008b6010 with catch @ 008bc054 */
                    /* catch() { ... } // from try @ 008b5fdc with catch @ 008bc058 */
        if (local_b0 == local_d0) {
          lVar8 = 0x20;
          plVar4 = local_d0;
LAB_008bc0b8:
          (**(code **)(*plVar4 + lVar8))();
        }
        else if (local_b0 != (long *)0x0) {
          lVar8 = 0x28;
          plVar4 = local_b0;
          goto LAB_008bc0b8;
        }
        FUN_008bbc90(&local_d8);
                    /* catch() { ... } // from try @ 008b224c with catch @ 008bc0d4 */
        if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
          FUN_00c54fec(uVar7);
        }
        goto LAB_008bc0ec;
      }
                    /* catch() { ... } // from try @ 008b5880 with catch @ 008bbeec */
      uVar9 = (long)param_1[5] - (long)pvVar11;
                    /* catch() { ... } // from try @ 008b578c with catch @ 008bbef0 */
                    /* catch() { ... } // from try @ 008b5780 with catch @ 008bbef4 */
      uVar10 = (long)uVar9 >> 2;
                    /* catch() { ... } // from try @ 008b576c with catch @ 008bbef8 */
                    /* catch() { ... } // from try @ 008b573c with catch @ 008bbefc */
      if (uVar10 <= uVar1) {
        uVar10 = uVar1;
      }
                    /* catch() { ... } // from try @ 008b5728 with catch @ 008bbf04 */
                    /* catch() { ... } // from try @ 008b8424 with catch @ 008bbf08 */
      if (0x7ffffffffffffff7 < uVar9) {
        uVar10 = 0x1fffffffffffffff;
      }
                    /* catch() { ... } // from try @ 008b8520 with catch @ 008bbf0c */
      if (uVar10 == 0) {
        pvVar5 = (void *)0x0;
      }
      else {
                    /* catch() { ... } // from try @ 008b3534 with catch @ 008bbf10 */
                    /* catch() { ... } // from try @ 008b3424 with catch @ 008bbf14 */
        if (uVar10 >> 0x3d != 0) {
LAB_008bc028:
                    /* catch() { ... } // from try @ 008b8720 with catch @ 008bc028 */
                    /* catch() { ... } // from try @ 008b8614 with catch @ 008bc02c */
                    /* catch() { ... } // from try @ 008b8328 with catch @ 008bc030 */
                    /* catch() { ... } // from try @ 008b6448 with catch @ 008bc034 */
          if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 008b6338 with catch @ 008bc038 */
            FUN_00441220();
          }
          goto LAB_008bc0ec;
        }
                    /* catch() { ... } // from try @ 008b330c with catch @ 008bbf18 */
                    /* catch() { ... } // from try @ 008b6658 with catch @ 008bbf1c */
        pvVar5 = (void *)_Znwm(uVar10 << 3);
                    /* catch() { ... } // from try @ 008b6620 with catch @ 008bbf20 */
      }
                    /* catch() { ... } // from try @ 008b95f4 with catch @ 008bbfc0 */
      puVar6 = (undefined8 *)((long)pvVar5 + lVar8 * 8);
                    /* catch() { ... } // from try @ 008b94e8 with catch @ 008bbfc4 */
                    /* catch() { ... } // from try @ 008b94b4 with catch @ 008bbfc8 */
                    /* catch() { ... } // from try @ 008b93c8 with catch @ 008bbfd0 */
      puVar12 = puVar6 + 1;
                    /* catch() { ... } // from try @ 008b9390 with catch @ 008bbfd4 */
      *puVar6 = puVar3;
      memcpy(pvVar5,pvVar11,(long)puVar13 - (long)pvVar11);
                    /* catch() { ... } // from try @ 008b9354 with catch @ 008bbfdc */
      param_1[3] = pvVar5;
      param_1[4] = puVar12;
                    /* catch() { ... } // from try @ 008b9288 with catch @ 008bbfe0 */
      param_1[5] = (void *)((long)pvVar5 + uVar10 * 8);
                    /* catch() { ... } // from try @ 008b927c with catch @ 008bbfe4 */
      if (pvVar11 != (void *)0x0) {
                    /* catch() { ... } // from try @ 008b918c with catch @ 008bbfe8 */
                    /* catch() { ... } // from try @ 008b9180 with catch @ 008bbfec */
        _ZdlPv(pvVar11);
      }
    }
                    /* catch() { ... } // from try @ 008b9088 with catch @ 008bbff0 */
    param_1[4] = puVar12;
  }
                    /* catch() { ... } // from try @ 008b907c with catch @ 008bbff4 */
                    /* catch() { ... } // from try @ 008b8f84 with catch @ 008bbff8 */
                    /* catch() { ... } // from try @ 008b8f78 with catch @ 008bbffc */
                    /* catch() { ... } // from try @ 008b8f48 with catch @ 008bc000 */
  if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 008b8e7c with catch @ 008bc004 */
                    /* catch() { ... } // from try @ 008b8e70 with catch @ 008bc008 */
                    /* catch() { ... } // from try @ 008b8e38 with catch @ 008bc00c */
                    /* catch() { ... } // from try @ 008b8d64 with catch @ 008bc010 */
                    /* catch() { ... } // from try @ 008b8d58 with catch @ 008bc014 */
                    /* catch() { ... } // from try @ 008b8a30 with catch @ 008bc018 */
                    /* catch() { ... } // from try @ 008b890c with catch @ 008bc01c */
                    /* catch() { ... } // from try @ 008b8818 with catch @ 008bc020 */
                    /* catch() { ... } // from try @ 008b8808 with catch @ 008bc024 */
    return puVar3;
  }
LAB_008bc0ec:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-008bbccc"></a> `008bbccc` | `ff 83 03 d1` | sub sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-008bbcd0"></a> `008bbcd0` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-008bbcd4"></a> `008bbcd4` | `fb 4b 00 f9` | str x27,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-008bbcd8"></a> `008bbcd8` | `fa 67 0a a9` | stp x26,x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-008bbcdc"></a> `008bbcdc` | `f8 5f 0b a9` | stp x24,x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-008bbce0"></a> `008bbce0` | `f6 57 0c a9` | stp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-008bbce4"></a> `008bbce4` | `f4 4f 0d a9` | stp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-008bbce8"></a> `008bbce8` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-008bbcec"></a> `008bbcec` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-008bbcf0"></a> `008bbcf0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-008bbcf4"></a> `008bbcf4` | `00 22 80 52` | mov w0,#0x110 | `FALL_THROUGH`
<a id="insn-008bbcf8"></a> `008bbcf8` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-008bbcfc"></a> `008bbcfc` | `f9 03 05 aa` | mov x25,x5 | `FALL_THROUGH`
<a id="insn-008bbd00"></a> `008bbd00` | `f5 03 04 2a` | mov w21,w4 | `FALL_THROUGH`
<a id="insn-008bbd04"></a> `008bbd04` | `f6 03 03 2a` | mov w22,w3 | `FALL_THROUGH`
<a id="insn-008bbd08"></a> `008bbd08` | `f7 03 02 2a` | mov w23,w2 | `FALL_THROUGH`
<a id="insn-008bbd0c"></a> `008bbd0c` | `f8 03 01 aa` | mov x24,x1 | `FALL_THROUGH`
<a id="insn-008bbd10"></a> `008bbd10` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008bbd14"></a> `008bbd14` | `87 74 0e 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-008bbd18"></a> `008bbd18` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-008bbd1c"></a> `008bbd1c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008bbd20"></a> `008bbd20` | `f3 07 00 f9` | str x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008bbd24"></a> `008bbd24` | `00 00 00 ad` | stp q0,q0,[x0] | `FALL_THROUGH`
<a id="insn-008bbd28"></a> `008bbd28` | `00 00 01 ad` | stp q0,q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-008bbd2c"></a> `008bbd2c` | `00 00 02 ad` | stp q0,q0,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-008bbd30"></a> `008bbd30` | `00 00 03 ad` | stp q0,q0,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-008bbd34"></a> `008bbd34` | `00 00 04 ad` | stp q0,q0,[x0, #0x80] | `FALL_THROUGH`
<a id="insn-008bbd38"></a> `008bbd38` | `00 00 05 ad` | stp q0,q0,[x0, #0xa0] | `FALL_THROUGH`
<a id="insn-008bbd3c"></a> `008bbd3c` | `00 00 06 ad` | stp q0,q0,[x0, #0xc0] | `FALL_THROUGH`
<a id="insn-008bbd40"></a> `008bbd40` | `00 00 07 ad` | stp q0,q0,[x0, #0xe0] | `FALL_THROUGH`
<a id="insn-008bbd44"></a> `008bbd44` | `20 13 40 f9` | ldr x0,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-008bbd48"></a> `008bbd48` | `60 42 80 3d` | str q0,[x19, #0x100] | `FALL_THROUGH`
<a id="insn-008bbd4c"></a> `008bbd4c` | `20 01 00 b4` | cbz x0,0x008bbd70 | `CONDITIONAL_JUMP`
<a id="insn-008bbd50"></a> `008bbd50` | `1f 00 19 eb` | cmp x0,x25 | `FALL_THROUGH`
<a id="insn-008bbd54"></a> `008bbd54` | `20 01 00 54` | b.eq 0x008bbd78 | `CONDITIONAL_JUMP`
<a id="insn-008bbd58"></a> `008bbd58` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-008bbd5c"></a> `008bbd5c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008bbd60"></a> `008bbd60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008bbd64"></a> `008bbd64` | `e0 1b 00 f9` | str x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008bbd68"></a> `008bbd68` | `a0 01 00 b5` | cbnz x0,0x008bbd9c | `CONDITIONAL_JUMP`
<a id="insn-008bbd6c"></a> `008bbd6c` | `12 00 00 14` | b 0x008bbdb4 | `UNCONDITIONAL_JUMP`
<a id="insn-008bbd70"></a> `008bbd70` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008bbd74"></a> `008bbd74` | `10 00 00 14` | b 0x008bbdb4 | `UNCONDITIONAL_JUMP`
<a id="insn-008bbd78"></a> `008bbd78` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008bbd7c"></a> `008bbd7c` | `29 03 40 f9` | ldr x9,[x25] | `FALL_THROUGH`
<a id="insn-008bbd80"></a> `008bbd80` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008bbd84"></a> `008bbd84` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-008bbd88"></a> `008bbd88` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008bbd8c"></a> `008bbd8c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-008bbd90"></a> `008bbd90` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008bbd94"></a> `008bbd94` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008bbd98"></a> `008bbd98` | `e0 00 00 b4` | cbz x0,0x008bbdb4 | `CONDITIONAL_JUMP`
<a id="insn-008bbd9c"></a> `008bbd9c` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008bbda0"></a> `008bbda0` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-008bbda4"></a> `008bbda4` | `20 0c 00 54` | b.eq 0x008bbf28 | `CONDITIONAL_JUMP`
<a id="insn-008bbda8"></a> `008bbda8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-008bbdac"></a> `008bbdac` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-008bbdb0"></a> `008bbdb0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008bbdb4"></a> `008bbdb4` | `e0 33 00 f9` | str x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008bbdb8"></a> `008bbdb8` | `e6 03 01 91` | add x6,sp,#0x40 | `FALL_THROUGH`
<a id="insn-008bbdbc"></a> `008bbdbc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008bbdc0"></a> `008bbdc0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-008bbdc4"></a> `008bbdc4` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-008bbdc8"></a> `008bbdc8` | `e3 03 17 2a` | mov w3,w23 | `FALL_THROUGH`
<a id="insn-008bbdcc"></a> `008bbdcc` | `e4 03 16 2a` | mov w4,w22 | `FALL_THROUGH`
<a id="insn-008bbdd0"></a> `008bbdd0` | `e5 03 15 2a` | mov w5,w21 | `FALL_THROUGH`
<a id="insn-008bbdd4"></a> `008bbdd4` | `e7 03 1f aa` | mov x7,xzr | `FALL_THROUGH`
<a id="insn-008bbdd8"></a> `008bbdd8` | `f6 03 01 91` | add x22,sp,#0x40 | `FALL_THROUGH`
<a id="insn-008bbddc"></a> `008bbddc` | `5f f5 ff 97` | bl 0x008b9358 | `UNCONDITIONAL_CALL`
<a id="insn-008bbde0"></a> `008bbde0` | `e0 33 40 f9` | ldr x0,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008bbde4"></a> `008bbde4` | `1f 00 16 eb` | cmp x0,x22 | `FALL_THROUGH`
<a id="insn-008bbde8"></a> `008bbde8` | `80 00 00 54` | b.eq 0x008bbdf8 | `CONDITIONAL_JUMP`
<a id="insn-008bbdec"></a> `008bbdec` | `00 01 00 b4` | cbz x0,0x008bbe0c | `CONDITIONAL_JUMP`
<a id="insn-008bbdf0"></a> `008bbdf0` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-008bbdf4"></a> `008bbdf4` | `03 00 00 14` | b 0x008bbe00 | `UNCONDITIONAL_JUMP`
<a id="insn-008bbdf8"></a> `008bbdf8` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-008bbdfc"></a> `008bbdfc` | `e0 03 01 91` | add x0,sp,#0x40 | `FALL_THROUGH`
<a id="insn-008bbe00"></a> `008bbe00` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-008bbe04"></a> `008bbe04` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008bbe08"></a> `008bbe08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008bbe0c"></a> `008bbe0c` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008bbe10"></a> `008bbe10` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008bbe14"></a> `008bbe14` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-008bbe18"></a> `008bbe18` | `80 00 00 54` | b.eq 0x008bbe28 | `CONDITIONAL_JUMP`
<a id="insn-008bbe1c"></a> `008bbe1c` | `00 01 00 b4` | cbz x0,0x008bbe3c | `CONDITIONAL_JUMP`
<a id="insn-008bbe20"></a> `008bbe20` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-008bbe24"></a> `008bbe24` | `03 00 00 14` | b 0x008bbe30 | `UNCONDITIONAL_JUMP`
<a id="insn-008bbe28"></a> `008bbe28` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-008bbe2c"></a> `008bbe2c` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008bbe30"></a> `008bbe30` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-008bbe34"></a> `008bbe34` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008bbe38"></a> `008bbe38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008bbe3c"></a> `008bbe3c` | `99 06 40 f9` | ldr x25,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-008bbe40"></a> `008bbe40` | `35 01 28 36` | tbz w21,#0x5,0x008bbe64 | `CONDITIONAL_JUMP`
<a id="insn-008bbe44"></a> `008bbe44` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-008bbe48"></a> `008bbe48` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-008bbe4c"></a> `008bbe4c` | `c0 00 00 54` | b.eq 0x008bbe64 | `CONDITIONAL_JUMP`
<a id="insn-008bbe50"></a> `008bbe50` | `98 22 42 a9` | ldp x24,x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-008bbe54"></a> `008bbe54` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-008bbe58"></a> `008bbe58` | `c2 03 00 54` | b.cs 0x008bbed0 | `CONDITIONAL_JUMP`
<a id="insn-008bbe5c"></a> `008bbe5c` | `13 87 00 f8` | str x19,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-008bbe60"></a> `008bbe60` | `64 00 00 14` | b 0x008bbff0 | `UNCONDITIONAL_JUMP`
<a id="insn-008bbe64"></a> `008bbe64` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-008bbe68"></a> `008bbe68` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-008bbe6c"></a> `008bbe6c` | `82 00 00 54` | b.cs 0x008bbe7c | `CONDITIONAL_JUMP`
<a id="insn-008bbe70"></a> `008bbe70` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008bbe74"></a> `008bbe74` | `33 87 00 f8` | str x19,[x25], #0x8 | `FALL_THROUGH`
<a id="insn-008bbe78"></a> `008bbe78` | `42 00 00 14` | b 0x008bbf80 | `UNCONDITIONAL_JUMP`
<a id="insn-008bbe7c"></a> `008bbe7c` | `96 02 40 f9` | ldr x22,[x20] | `FALL_THROUGH`
<a id="insn-008bbe80"></a> `008bbe80` | `37 03 16 cb` | sub x23,x25,x22 | `FALL_THROUGH`
<a id="insn-008bbe84"></a> `008bbe84` | `f9 fe 43 93` | asr x25,x23,#0x3 | `FALL_THROUGH`
<a id="insn-008bbe88"></a> `008bbe88` | `29 07 00 91` | add x9,x25,#0x1 | `FALL_THROUGH`
<a id="insn-008bbe8c"></a> `008bbe8c` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-008bbe90"></a> `008bbe90` | `6a 0d 00 b5` | cbnz x10,0x008bc03c | `CONDITIONAL_JUMP`
<a id="insn-008bbe94"></a> `008bbe94` | `08 01 16 cb` | sub x8,x8,x22 | `FALL_THROUGH`
<a id="insn-008bbe98"></a> `008bbe98` | `eb ef 7d b2` | orr x11,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-008bbe9c"></a> `008bbe9c` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-008bbea0"></a> `008bbea0` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-008bbea4"></a> `008bbea4` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-008bbea8"></a> `008bbea8` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-008bbeac"></a> `008bbeac` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-008bbeb0"></a> `008bbeb0` | `3b 31 88 9a` | csel x27,x9,x8,cc | `FALL_THROUGH`
<a id="insn-008bbeb4"></a> `008bbeb4` | `bb 04 00 b4` | cbz x27,0x008bbf48 | `CONDITIONAL_JUMP`
<a id="insn-008bbeb8"></a> `008bbeb8` | `68 ff 7d d3` | lsr x8,x27,#0x3d | `FALL_THROUGH`
<a id="insn-008bbebc"></a> `008bbebc` | `68 0b 00 b5` | cbnz x8,0x008bc028 | `CONDITIONAL_JUMP`
<a id="insn-008bbec0"></a> `008bbec0` | `60 f3 7d d3` | lsl x0,x27,#0x3 | `FALL_THROUGH`
<a id="insn-008bbec4"></a> `008bbec4` | `1b 74 0e 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-008bbec8"></a> `008bbec8` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-008bbecc"></a> `008bbecc` | `20 00 00 14` | b 0x008bbf4c | `UNCONDITIONAL_JUMP`
<a id="insn-008bbed0"></a> `008bbed0` | `80 62 00 91` | add x0,x20,#0x18 | `FALL_THROUGH`
<a id="insn-008bbed4"></a> `008bbed4` | `15 00 40 f9` | ldr x21,[x0] | `FALL_THROUGH`
<a id="insn-008bbed8"></a> `008bbed8` | `16 03 15 cb` | sub x22,x24,x21 | `FALL_THROUGH`
<a id="insn-008bbedc"></a> `008bbedc` | `d8 fe 43 93` | asr x24,x22,#0x3 | `FALL_THROUGH`
<a id="insn-008bbee0"></a> `008bbee0` | `09 07 00 91` | add x9,x24,#0x1 | `FALL_THROUGH`
<a id="insn-008bbee4"></a> `008bbee4` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-008bbee8"></a> `008bbee8` | `ca 0a 00 b5` | cbnz x10,0x008bc040 | `CONDITIONAL_JUMP`
<a id="insn-008bbeec"></a> `008bbeec` | `08 01 15 cb` | sub x8,x8,x21 | `FALL_THROUGH`
<a id="insn-008bbef0"></a> `008bbef0` | `eb ef 7d b2` | orr x11,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-008bbef4"></a> `008bbef4` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-008bbef8"></a> `008bbef8` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-008bbefc"></a> `008bbefc` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-008bbf00"></a> `008bbf00` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-008bbf04"></a> `008bbf04` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-008bbf08"></a> `008bbf08` | `39 31 88 9a` | csel x25,x9,x8,cc | `FALL_THROUGH`
<a id="insn-008bbf0c"></a> `008bbf0c` | `99 05 00 b4` | cbz x25,0x008bbfbc | `CONDITIONAL_JUMP`
<a id="insn-008bbf10"></a> `008bbf10` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-008bbf14"></a> `008bbf14` | `a8 08 00 b5` | cbnz x8,0x008bc028 | `CONDITIONAL_JUMP`
<a id="insn-008bbf18"></a> `008bbf18` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-008bbf1c"></a> `008bbf1c` | `05 74 0e 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-008bbf20"></a> `008bbf20` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-008bbf24"></a> `008bbf24` | `27 00 00 14` | b 0x008bbfc0 | `UNCONDITIONAL_JUMP`
<a id="insn-008bbf28"></a> `008bbf28` | `e8 03 01 91` | add x8,sp,#0x40 | `FALL_THROUGH`
<a id="insn-008bbf2c"></a> `008bbf2c` | `e9 0b 40 f9` | ldr x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-008bbf30"></a> `008bbf30` | `e8 33 00 f9` | str x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-008bbf34"></a> `008bbf34` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-008bbf38"></a> `008bbf38` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008bbf3c"></a> `008bbf3c` | `e1 03 01 91` | add x1,sp,#0x40 | `FALL_THROUGH`
<a id="insn-008bbf40"></a> `008bbf40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008bbf44"></a> `008bbf44` | `9d ff ff 17` | b 0x008bbdb8 | `UNCONDITIONAL_JUMP`
<a id="insn-008bbf48"></a> `008bbf48` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-008bbf4c"></a> `008bbf4c` | `19 0f 19 8b` | add x25,x24,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-008bbf50"></a> `008bbf50` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-008bbf54"></a> `008bbf54` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-008bbf58"></a> `008bbf58` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-008bbf5c"></a> `008bbf5c` | `1b 0f 1b 8b` | add x27,x24,x27, LSL #0x3 | `FALL_THROUGH`
<a id="insn-008bbf60"></a> `008bbf60` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-008bbf64"></a> `008bbf64` | `33 87 00 f8` | str x19,[x25], #0x8 | `FALL_THROUGH`
<a id="insn-008bbf68"></a> `008bbf68` | `4e 74 0e 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-008bbf6c"></a> `008bbf6c` | `98 66 00 a9` | stp x24,x25,[x20] | `FALL_THROUGH`
<a id="insn-008bbf70"></a> `008bbf70` | `9b 0a 00 f9` | str x27,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-008bbf74"></a> `008bbf74` | `76 00 00 b4` | cbz x22,0x008bbf80 | `CONDITIONAL_JUMP`
<a id="insn-008bbf78"></a> `008bbf78` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-008bbf7c"></a> `008bbf7c` | `f5 73 0e 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-008bbf80"></a> `008bbf80` | `99 06 00 f9` | str x25,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-008bbf84"></a> `008bbf84` | `95 03 30 37` | tbnz w21,#0x6,0x008bbff4 | `CONDITIONAL_JUMP`
<a id="insn-008bbf88"></a> `008bbf88` | `5d 59 fe 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-008bbf8c"></a> `008bbf8c` | `c8 ae 86 52` | mov w8,#0x3576 | `FALL_THROUGH`
<a id="insn-008bbf90"></a> `008bbf90` | `1f 68 28 38` | strb wzr,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-008bbf94"></a> `008bbf94` | `5a 59 fe 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-008bbf98"></a> `008bbf98` | `08 ae 86 52` | mov w8,#0x3570 | `FALL_THROUGH`
<a id="insn-008bbf9c"></a> `008bbf9c` | `1f 68 28 38` | strb wzr,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-008bbfa0"></a> `008bbfa0` | `57 59 fe 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-008bbfa4"></a> `008bbfa4` | `68 ae 86 52` | mov w8,#0x3573 | `FALL_THROUGH`
<a id="insn-008bbfa8"></a> `008bbfa8` | `1f 68 28 38` | strb wzr,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-008bbfac"></a> `008bbfac` | `54 59 fe 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-008bbfb0"></a> `008bbfb0` | `48 ae 86 52` | mov w8,#0x3572 | `FALL_THROUGH`
<a id="insn-008bbfb4"></a> `008bbfb4` | `1f 68 28 38` | strb wzr,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-008bbfb8"></a> `008bbfb8` | `0f 00 00 14` | b 0x008bbff4 | `UNCONDITIONAL_JUMP`
<a id="insn-008bbfbc"></a> `008bbfbc` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-008bbfc0"></a> `008bbfc0` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-008bbfc4"></a> `008bbfc4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-008bbfc8"></a> `008bbfc8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-008bbfcc"></a> `008bbfcc` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-008bbfd0"></a> `008bbfd0` | `f9 0e 19 8b` | add x25,x23,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-008bbfd4"></a> `008bbfd4` | `13 87 00 f8` | str x19,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-008bbfd8"></a> `008bbfd8` | `32 74 0e 94` | bl 0x00c590a0 | `UNCONDITIONAL_CALL`
<a id="insn-008bbfdc"></a> `008bbfdc` | `97 e2 01 a9` | stp x23,x24,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-008bbfe0"></a> `008bbfe0` | `99 16 00 f9` | str x25,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-008bbfe4"></a> `008bbfe4` | `75 00 00 b4` | cbz x21,0x008bbff0 | `CONDITIONAL_JUMP`
<a id="insn-008bbfe8"></a> `008bbfe8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-008bbfec"></a> `008bbfec` | `d9 73 0e 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-008bbff0"></a> `008bbff0` | `98 12 00 f9` | str x24,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-008bbff4"></a> `008bbff4` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-008bbff8"></a> `008bbff8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008bbffc"></a> `008bbffc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008bc000"></a> `008bc000` | `61 07 00 54` | b.ne 0x008bc0ec | `CONDITIONAL_JUMP`
<a id="insn-008bc004"></a> `008bc004` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008bc008"></a> `008bc008` | `f4 4f 4d a9` | ldp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-008bc00c"></a> `008bc00c` | `fb 4b 40 f9` | ldr x27,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-008bc010"></a> `008bc010` | `f6 57 4c a9` | ldp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-008bc014"></a> `008bc014` | `f8 5f 4b a9` | ldp x24,x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-008bc018"></a> `008bc018` | `fa 67 4a a9` | ldp x26,x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-008bc01c"></a> `008bc01c` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-008bc020"></a> `008bc020` | `ff 83 03 91` | add sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-008bc024"></a> `008bc024` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-008bc028"></a> `008bc028` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-008bc02c"></a> `008bc02c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008bc030"></a> `008bc030` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008bc034"></a> `008bc034` | `c1 05 00 54` | b.ne 0x008bc0ec | `CONDITIONAL_JUMP`
<a id="insn-008bc038"></a> `008bc038` | `7a 14 ee 97` | bl 0x00441220 | `CALL_TERMINATOR`
<a id="insn-008bc03c"></a> `008bc03c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-008bc040"></a> `008bc040` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-008bc044"></a> `008bc044` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008bc048"></a> `008bc048` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008bc04c"></a> `008bc04c` | `01 05 00 54` | b.ne 0x008bc0ec | `CONDITIONAL_JUMP`
<a id="insn-008bc050"></a> `008bc050` | `31 05 00 94` | bl 0x008bd514 | `UNCONDITIONAL_CALL`
<a id="insn-008bc054"></a> `008bc054` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-008bc058"></a> `008bc058` | `0f 00 00 14` | b 0x008bc094 | `UNCONDITIONAL_JUMP`
<a id="insn-008bc094"></a> `008bc094` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-008bc098"></a> `008bc098` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008bc09c"></a> `008bc09c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-008bc0a0"></a> `008bc0a0` | `81 00 00 54` | b.ne 0x008bc0b0 | `CONDITIONAL_JUMP`
<a id="insn-008bc0a4"></a> `008bc0a4` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-008bc0a8"></a> `008bc0a8` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-008bc0ac"></a> `008bc0ac` | `03 00 00 14` | b 0x008bc0b8 | `UNCONDITIONAL_JUMP`
<a id="insn-008bc0b0"></a> `008bc0b0` | `e0 00 00 b4` | cbz x0,0x008bc0cc | `CONDITIONAL_JUMP`
<a id="insn-008bc0b4"></a> `008bc0b4` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-008bc0b8"></a> `008bc0b8` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-008bc0bc"></a> `008bc0bc` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-008bc0c0"></a> `008bc0c0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-008bc0c4"></a> `008bc0c4` | `02 00 00 14` | b 0x008bc0cc | `UNCONDITIONAL_JUMP`
<a id="insn-008bc0cc"></a> `008bc0cc` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-008bc0d0"></a> `008bc0d0` | `f0 fe ff 97` | bl 0x008bbc90 | `UNCONDITIONAL_CALL`
<a id="insn-008bc0d4"></a> `008bc0d4` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-008bc0d8"></a> `008bc0d8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-008bc0dc"></a> `008bc0dc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-008bc0e0"></a> `008bc0e0` | `61 00 00 54` | b.ne 0x008bc0ec | `CONDITIONAL_JUMP`
<a id="insn-008bc0e4"></a> `008bc0e4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-008bc0e8"></a> `008bc0e8` | `c1 63 0e 94` | bl 0x00c54fec | `CALL_TERMINATOR`
<a id="insn-008bc0ec"></a> `008bc0ec` | `a5 73 0e 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`008bbccc`](#insn-008bbccc) 範囲 `[['008bbccc', '008bbd4f']]`
  - `CONDITIONAL_JUMP` [`008bbd4c`](#insn-008bbd4c) → [`008bbd70`](#insn-008bbd70)
  - `FALL_THROUGH` [`008bbd4c`](#insn-008bbd4c) → [`008bbd50`](#insn-008bbd50)
- ブロック [`008bbd50`](#insn-008bbd50) 範囲 `[['008bbd50', '008bbd57']]`
  - `CONDITIONAL_JUMP` [`008bbd54`](#insn-008bbd54) → [`008bbd78`](#insn-008bbd78)
  - `FALL_THROUGH` [`008bbd54`](#insn-008bbd54) → [`008bbd58`](#insn-008bbd58)
- ブロック [`008bbd58`](#insn-008bbd58) 範囲 `[['008bbd58', '008bbd6b']]`
  - `CONDITIONAL_JUMP` [`008bbd68`](#insn-008bbd68) → [`008bbd9c`](#insn-008bbd9c)
  - `FALL_THROUGH` [`008bbd68`](#insn-008bbd68) → [`008bbd6c`](#insn-008bbd6c)
- ブロック [`008bbd6c`](#insn-008bbd6c) 範囲 `[['008bbd6c', '008bbd6f']]`
  - `UNCONDITIONAL_JUMP` [`008bbd6c`](#insn-008bbd6c) → [`008bbdb4`](#insn-008bbdb4)
- ブロック [`008bbd70`](#insn-008bbd70) 範囲 `[['008bbd70', '008bbd77']]`
  - `UNCONDITIONAL_JUMP` [`008bbd74`](#insn-008bbd74) → [`008bbdb4`](#insn-008bbdb4)
- ブロック [`008bbd78`](#insn-008bbd78) 範囲 `[['008bbd78', '008bbd9b']]`
  - `CONDITIONAL_JUMP` [`008bbd98`](#insn-008bbd98) → [`008bbdb4`](#insn-008bbdb4)
  - `FALL_THROUGH` [`008bbd98`](#insn-008bbd98) → [`008bbd9c`](#insn-008bbd9c)
- ブロック [`008bbd9c`](#insn-008bbd9c) 範囲 `[['008bbd9c', '008bbda7']]`
  - `CONDITIONAL_JUMP` [`008bbda4`](#insn-008bbda4) → [`008bbf28`](#insn-008bbf28)
  - `FALL_THROUGH` [`008bbda4`](#insn-008bbda4) → [`008bbda8`](#insn-008bbda8)
- ブロック [`008bbda8`](#insn-008bbda8) 範囲 `[['008bbda8', '008bbdb3']]`
  - `FALL_THROUGH` [`008bbdb0`](#insn-008bbdb0) → [`008bbdb4`](#insn-008bbdb4)
- ブロック [`008bbdb4`](#insn-008bbdb4) 範囲 `[['008bbdb4', '008bbdb7']]`
  - `FALL_THROUGH` [`008bbdb4`](#insn-008bbdb4) → [`008bbdb8`](#insn-008bbdb8)
- ブロック [`008bbdb8`](#insn-008bbdb8) 範囲 `[['008bbdb8', '008bbddb']]`
  - `FALL_THROUGH` [`008bbdd8`](#insn-008bbdd8) → [`008bbddc`](#insn-008bbddc)
- ブロック [`008bbddc`](#insn-008bbddc) 範囲 `[['008bbddc', '008bbddf']]`
  - `FALL_THROUGH` [`008bbddc`](#insn-008bbddc) → [`008bbde0`](#insn-008bbde0)
- ブロック [`008bbde0`](#insn-008bbde0) 範囲 `[['008bbde0', '008bbde7']]`
  - `FALL_THROUGH` [`008bbde4`](#insn-008bbde4) → [`008bbde8`](#insn-008bbde8)
- ブロック [`008bbde8`](#insn-008bbde8) 範囲 `[['008bbde8', '008bbdeb']]`
  - `CONDITIONAL_JUMP` [`008bbde8`](#insn-008bbde8) → [`008bbdf8`](#insn-008bbdf8)
  - `FALL_THROUGH` [`008bbde8`](#insn-008bbde8) → [`008bbdec`](#insn-008bbdec)
- ブロック [`008bbdec`](#insn-008bbdec) 範囲 `[['008bbdec', '008bbdef']]`
  - `CONDITIONAL_JUMP` [`008bbdec`](#insn-008bbdec) → [`008bbe0c`](#insn-008bbe0c)
  - `FALL_THROUGH` [`008bbdec`](#insn-008bbdec) → [`008bbdf0`](#insn-008bbdf0)
- ブロック [`008bbdf0`](#insn-008bbdf0) 範囲 `[['008bbdf0', '008bbdf3']]`
  - `FALL_THROUGH` [`008bbdf0`](#insn-008bbdf0) → [`008bbdf4`](#insn-008bbdf4)
- ブロック [`008bbdf4`](#insn-008bbdf4) 範囲 `[['008bbdf4', '008bbdf7']]`
  - `UNCONDITIONAL_JUMP` [`008bbdf4`](#insn-008bbdf4) → [`008bbe00`](#insn-008bbe00)
- ブロック [`008bbdf8`](#insn-008bbdf8) 範囲 `[['008bbdf8', '008bbdfb']]`
  - `FALL_THROUGH` [`008bbdf8`](#insn-008bbdf8) → [`008bbdfc`](#insn-008bbdfc)
- ブロック [`008bbdfc`](#insn-008bbdfc) 範囲 `[['008bbdfc', '008bbdff']]`
  - `FALL_THROUGH` [`008bbdfc`](#insn-008bbdfc) → [`008bbe00`](#insn-008bbe00)
- ブロック [`008bbe00`](#insn-008bbe00) 範囲 `[['008bbe00', '008bbe03']]`
  - `FALL_THROUGH` [`008bbe00`](#insn-008bbe00) → [`008bbe04`](#insn-008bbe04)
- ブロック [`008bbe04`](#insn-008bbe04) 範囲 `[['008bbe04', '008bbe07']]`
  - `FALL_THROUGH` [`008bbe04`](#insn-008bbe04) → [`008bbe08`](#insn-008bbe08)
- ブロック [`008bbe08`](#insn-008bbe08) 範囲 `[['008bbe08', '008bbe0b']]`
  - `FALL_THROUGH` [`008bbe08`](#insn-008bbe08) → [`008bbe0c`](#insn-008bbe0c)
- ブロック [`008bbe0c`](#insn-008bbe0c) 範囲 `[['008bbe0c', '008bbe0f']]`
  - `FALL_THROUGH` [`008bbe0c`](#insn-008bbe0c) → [`008bbe10`](#insn-008bbe10)
- ブロック [`008bbe10`](#insn-008bbe10) 範囲 `[['008bbe10', '008bbe13']]`
  - `FALL_THROUGH` [`008bbe10`](#insn-008bbe10) → [`008bbe14`](#insn-008bbe14)
- ブロック [`008bbe14`](#insn-008bbe14) 範囲 `[['008bbe14', '008bbe17']]`
  - `FALL_THROUGH` [`008bbe14`](#insn-008bbe14) → [`008bbe18`](#insn-008bbe18)
- ブロック [`008bbe18`](#insn-008bbe18) 範囲 `[['008bbe18', '008bbe1b']]`
  - `CONDITIONAL_JUMP` [`008bbe18`](#insn-008bbe18) → [`008bbe28`](#insn-008bbe28)
  - `FALL_THROUGH` [`008bbe18`](#insn-008bbe18) → [`008bbe1c`](#insn-008bbe1c)
- ブロック [`008bbe1c`](#insn-008bbe1c) 範囲 `[['008bbe1c', '008bbe1f']]`
  - `CONDITIONAL_JUMP` [`008bbe1c`](#insn-008bbe1c) → [`008bbe3c`](#insn-008bbe3c)
  - `FALL_THROUGH` [`008bbe1c`](#insn-008bbe1c) → [`008bbe20`](#insn-008bbe20)
- ブロック [`008bbe20`](#insn-008bbe20) 範囲 `[['008bbe20', '008bbe23']]`
  - `FALL_THROUGH` [`008bbe20`](#insn-008bbe20) → [`008bbe24`](#insn-008bbe24)
- ブロック [`008bbe24`](#insn-008bbe24) 範囲 `[['008bbe24', '008bbe27']]`
  - `UNCONDITIONAL_JUMP` [`008bbe24`](#insn-008bbe24) → [`008bbe30`](#insn-008bbe30)
- ブロック [`008bbe28`](#insn-008bbe28) 範囲 `[['008bbe28', '008bbe2f']]`
  - `FALL_THROUGH` [`008bbe2c`](#insn-008bbe2c) → [`008bbe30`](#insn-008bbe30)
- ブロック [`008bbe30`](#insn-008bbe30) 範囲 `[['008bbe30', '008bbe33']]`
  - `FALL_THROUGH` [`008bbe30`](#insn-008bbe30) → [`008bbe34`](#insn-008bbe34)
- ブロック [`008bbe34`](#insn-008bbe34) 範囲 `[['008bbe34', '008bbe37']]`
  - `FALL_THROUGH` [`008bbe34`](#insn-008bbe34) → [`008bbe38`](#insn-008bbe38)
- ブロック [`008bbe38`](#insn-008bbe38) 範囲 `[['008bbe38', '008bbe3b']]`
  - `FALL_THROUGH` [`008bbe38`](#insn-008bbe38) → [`008bbe3c`](#insn-008bbe3c)
- ブロック [`008bbe3c`](#insn-008bbe3c) 範囲 `[['008bbe3c', '008bbe43']]`
  - `CONDITIONAL_JUMP` [`008bbe40`](#insn-008bbe40) → [`008bbe64`](#insn-008bbe64)
  - `FALL_THROUGH` [`008bbe40`](#insn-008bbe40) → [`008bbe44`](#insn-008bbe44)
- ブロック [`008bbe44`](#insn-008bbe44) 範囲 `[['008bbe44', '008bbe47']]`
  - `FALL_THROUGH` [`008bbe44`](#insn-008bbe44) → [`008bbe48`](#insn-008bbe48)
- ブロック [`008bbe48`](#insn-008bbe48) 範囲 `[['008bbe48', '008bbe4b']]`
  - `FALL_THROUGH` [`008bbe48`](#insn-008bbe48) → [`008bbe4c`](#insn-008bbe4c)
- ブロック [`008bbe4c`](#insn-008bbe4c) 範囲 `[['008bbe4c', '008bbe4f']]`
  - `CONDITIONAL_JUMP` [`008bbe4c`](#insn-008bbe4c) → [`008bbe64`](#insn-008bbe64)
  - `FALL_THROUGH` [`008bbe4c`](#insn-008bbe4c) → [`008bbe50`](#insn-008bbe50)
- ブロック [`008bbe50`](#insn-008bbe50) 範囲 `[['008bbe50', '008bbe57']]`
  - `FALL_THROUGH` [`008bbe54`](#insn-008bbe54) → [`008bbe58`](#insn-008bbe58)
- ブロック [`008bbe58`](#insn-008bbe58) 範囲 `[['008bbe58', '008bbe5b']]`
  - `CONDITIONAL_JUMP` [`008bbe58`](#insn-008bbe58) → [`008bbed0`](#insn-008bbed0)
  - `FALL_THROUGH` [`008bbe58`](#insn-008bbe58) → [`008bbe5c`](#insn-008bbe5c)
- ブロック [`008bbe5c`](#insn-008bbe5c) 範囲 `[['008bbe5c', '008bbe5f']]`
  - `FALL_THROUGH` [`008bbe5c`](#insn-008bbe5c) → [`008bbe60`](#insn-008bbe60)
- ブロック [`008bbe60`](#insn-008bbe60) 範囲 `[['008bbe60', '008bbe63']]`
  - `UNCONDITIONAL_JUMP` [`008bbe60`](#insn-008bbe60) → [`008bbff0`](#insn-008bbff0)
- ブロック [`008bbe64`](#insn-008bbe64) 範囲 `[['008bbe64', '008bbe6b']]`
  - `FALL_THROUGH` [`008bbe68`](#insn-008bbe68) → [`008bbe6c`](#insn-008bbe6c)
- ブロック [`008bbe6c`](#insn-008bbe6c) 範囲 `[['008bbe6c', '008bbe6f']]`
  - `CONDITIONAL_JUMP` [`008bbe6c`](#insn-008bbe6c) → [`008bbe7c`](#insn-008bbe7c)
  - `FALL_THROUGH` [`008bbe6c`](#insn-008bbe6c) → [`008bbe70`](#insn-008bbe70)
- ブロック [`008bbe70`](#insn-008bbe70) 範囲 `[['008bbe70', '008bbe77']]`
  - `FALL_THROUGH` [`008bbe74`](#insn-008bbe74) → [`008bbe78`](#insn-008bbe78)
- ブロック [`008bbe78`](#insn-008bbe78) 範囲 `[['008bbe78', '008bbe7b']]`
  - `UNCONDITIONAL_JUMP` [`008bbe78`](#insn-008bbe78) → [`008bbf80`](#insn-008bbf80)
- ブロック [`008bbe7c`](#insn-008bbe7c) 範囲 `[['008bbe7c', '008bbe83']]`
  - `FALL_THROUGH` [`008bbe80`](#insn-008bbe80) → [`008bbe84`](#insn-008bbe84)
- ブロック [`008bbe84`](#insn-008bbe84) 範囲 `[['008bbe84', '008bbe87']]`
  - `FALL_THROUGH` [`008bbe84`](#insn-008bbe84) → [`008bbe88`](#insn-008bbe88)
- ブロック [`008bbe88`](#insn-008bbe88) 範囲 `[['008bbe88', '008bbe8b']]`
  - `FALL_THROUGH` [`008bbe88`](#insn-008bbe88) → [`008bbe8c`](#insn-008bbe8c)
- ブロック [`008bbe8c`](#insn-008bbe8c) 範囲 `[['008bbe8c', '008bbe8f']]`
  - `FALL_THROUGH` [`008bbe8c`](#insn-008bbe8c) → [`008bbe90`](#insn-008bbe90)
- ブロック [`008bbe90`](#insn-008bbe90) 範囲 `[['008bbe90', '008bbe93']]`
  - `CONDITIONAL_JUMP` [`008bbe90`](#insn-008bbe90) → [`008bc03c`](#insn-008bc03c)
  - `FALL_THROUGH` [`008bbe90`](#insn-008bbe90) → [`008bbe94`](#insn-008bbe94)
- ブロック [`008bbe94`](#insn-008bbe94) 範囲 `[['008bbe94', '008bbe97']]`
  - `FALL_THROUGH` [`008bbe94`](#insn-008bbe94) → [`008bbe98`](#insn-008bbe98)
- ブロック [`008bbe98`](#insn-008bbe98) 範囲 `[['008bbe98', '008bbe9b']]`
  - `FALL_THROUGH` [`008bbe98`](#insn-008bbe98) → [`008bbe9c`](#insn-008bbe9c)
- ブロック [`008bbe9c`](#insn-008bbe9c) 範囲 `[['008bbe9c', '008bbe9f']]`
  - `FALL_THROUGH` [`008bbe9c`](#insn-008bbe9c) → [`008bbea0`](#insn-008bbea0)
- ブロック [`008bbea0`](#insn-008bbea0) 範囲 `[['008bbea0', '008bbea3']]`
  - `FALL_THROUGH` [`008bbea0`](#insn-008bbea0) → [`008bbea4`](#insn-008bbea4)
- ブロック [`008bbea4`](#insn-008bbea4) 範囲 `[['008bbea4', '008bbea7']]`
  - `FALL_THROUGH` [`008bbea4`](#insn-008bbea4) → [`008bbea8`](#insn-008bbea8)
- ブロック [`008bbea8`](#insn-008bbea8) 範囲 `[['008bbea8', '008bbeaf']]`
  - `FALL_THROUGH` [`008bbeac`](#insn-008bbeac) → [`008bbeb0`](#insn-008bbeb0)
- ブロック [`008bbeb0`](#insn-008bbeb0) 範囲 `[['008bbeb0', '008bbeb7']]`
  - `CONDITIONAL_JUMP` [`008bbeb4`](#insn-008bbeb4) → [`008bbf48`](#insn-008bbf48)
  - `FALL_THROUGH` [`008bbeb4`](#insn-008bbeb4) → [`008bbeb8`](#insn-008bbeb8)
- ブロック [`008bbeb8`](#insn-008bbeb8) 範囲 `[['008bbeb8', '008bbebb']]`
  - `FALL_THROUGH` [`008bbeb8`](#insn-008bbeb8) → [`008bbebc`](#insn-008bbebc)
- ブロック [`008bbebc`](#insn-008bbebc) 範囲 `[['008bbebc', '008bbebf']]`
  - `CONDITIONAL_JUMP` [`008bbebc`](#insn-008bbebc) → [`008bc028`](#insn-008bc028)
  - `FALL_THROUGH` [`008bbebc`](#insn-008bbebc) → [`008bbec0`](#insn-008bbec0)
- ブロック [`008bbec0`](#insn-008bbec0) 範囲 `[['008bbec0', '008bbec7']]`
  - `FALL_THROUGH` [`008bbec4`](#insn-008bbec4) → [`008bbec8`](#insn-008bbec8)
- ブロック [`008bbec8`](#insn-008bbec8) 範囲 `[['008bbec8', '008bbecb']]`
  - `FALL_THROUGH` [`008bbec8`](#insn-008bbec8) → [`008bbecc`](#insn-008bbecc)
- ブロック [`008bbecc`](#insn-008bbecc) 範囲 `[['008bbecc', '008bbecf']]`
  - `UNCONDITIONAL_JUMP` [`008bbecc`](#insn-008bbecc) → [`008bbf4c`](#insn-008bbf4c)
- ブロック [`008bbed0`](#insn-008bbed0) 範囲 `[['008bbed0', '008bbed3']]`
  - `FALL_THROUGH` [`008bbed0`](#insn-008bbed0) → [`008bbed4`](#insn-008bbed4)
- ブロック [`008bbed4`](#insn-008bbed4) 範囲 `[['008bbed4', '008bbed7']]`
  - `FALL_THROUGH` [`008bbed4`](#insn-008bbed4) → [`008bbed8`](#insn-008bbed8)
- ブロック [`008bbed8`](#insn-008bbed8) 範囲 `[['008bbed8', '008bbedb']]`
  - `FALL_THROUGH` [`008bbed8`](#insn-008bbed8) → [`008bbedc`](#insn-008bbedc)
- ブロック [`008bbedc`](#insn-008bbedc) 範囲 `[['008bbedc', '008bbedf']]`
  - `FALL_THROUGH` [`008bbedc`](#insn-008bbedc) → [`008bbee0`](#insn-008bbee0)
- ブロック [`008bbee0`](#insn-008bbee0) 範囲 `[['008bbee0', '008bbee3']]`
  - `FALL_THROUGH` [`008bbee0`](#insn-008bbee0) → [`008bbee4`](#insn-008bbee4)
- ブロック [`008bbee4`](#insn-008bbee4) 範囲 `[['008bbee4', '008bbeeb']]`
  - `CONDITIONAL_JUMP` [`008bbee8`](#insn-008bbee8) → [`008bc040`](#insn-008bc040)
  - `FALL_THROUGH` [`008bbee8`](#insn-008bbee8) → [`008bbeec`](#insn-008bbeec)
- ブロック [`008bbeec`](#insn-008bbeec) 範囲 `[['008bbeec', '008bbeef']]`
  - `FALL_THROUGH` [`008bbeec`](#insn-008bbeec) → [`008bbef0`](#insn-008bbef0)
- ブロック [`008bbef0`](#insn-008bbef0) 範囲 `[['008bbef0', '008bbef3']]`
  - `FALL_THROUGH` [`008bbef0`](#insn-008bbef0) → [`008bbef4`](#insn-008bbef4)
- ブロック [`008bbef4`](#insn-008bbef4) 範囲 `[['008bbef4', '008bbef7']]`
  - `FALL_THROUGH` [`008bbef4`](#insn-008bbef4) → [`008bbef8`](#insn-008bbef8)
- ブロック [`008bbef8`](#insn-008bbef8) 範囲 `[['008bbef8', '008bbefb']]`
  - `FALL_THROUGH` [`008bbef8`](#insn-008bbef8) → [`008bbefc`](#insn-008bbefc)
- ブロック [`008bbefc`](#insn-008bbefc) 範囲 `[['008bbefc', '008bbf03']]`
  - `FALL_THROUGH` [`008bbf00`](#insn-008bbf00) → [`008bbf04`](#insn-008bbf04)
- ブロック [`008bbf04`](#insn-008bbf04) 範囲 `[['008bbf04', '008bbf07']]`
  - `FALL_THROUGH` [`008bbf04`](#insn-008bbf04) → [`008bbf08`](#insn-008bbf08)
- ブロック [`008bbf08`](#insn-008bbf08) 範囲 `[['008bbf08', '008bbf0b']]`
  - `FALL_THROUGH` [`008bbf08`](#insn-008bbf08) → [`008bbf0c`](#insn-008bbf0c)
- ブロック [`008bbf0c`](#insn-008bbf0c) 範囲 `[['008bbf0c', '008bbf0f']]`
  - `CONDITIONAL_JUMP` [`008bbf0c`](#insn-008bbf0c) → [`008bbfbc`](#insn-008bbfbc)
  - `FALL_THROUGH` [`008bbf0c`](#insn-008bbf0c) → [`008bbf10`](#insn-008bbf10)
- ブロック [`008bbf10`](#insn-008bbf10) 範囲 `[['008bbf10', '008bbf13']]`
  - `FALL_THROUGH` [`008bbf10`](#insn-008bbf10) → [`008bbf14`](#insn-008bbf14)
- ブロック [`008bbf14`](#insn-008bbf14) 範囲 `[['008bbf14', '008bbf17']]`
  - `CONDITIONAL_JUMP` [`008bbf14`](#insn-008bbf14) → [`008bc028`](#insn-008bc028)
  - `FALL_THROUGH` [`008bbf14`](#insn-008bbf14) → [`008bbf18`](#insn-008bbf18)
- ブロック [`008bbf18`](#insn-008bbf18) 範囲 `[['008bbf18', '008bbf1b']]`
  - `FALL_THROUGH` [`008bbf18`](#insn-008bbf18) → [`008bbf1c`](#insn-008bbf1c)
- ブロック [`008bbf1c`](#insn-008bbf1c) 範囲 `[['008bbf1c', '008bbf1f']]`
  - `FALL_THROUGH` [`008bbf1c`](#insn-008bbf1c) → [`008bbf20`](#insn-008bbf20)
- ブロック [`008bbf20`](#insn-008bbf20) 範囲 `[['008bbf20', '008bbf27']]`
  - `UNCONDITIONAL_JUMP` [`008bbf24`](#insn-008bbf24) → [`008bbfc0`](#insn-008bbfc0)
- ブロック [`008bbf28`](#insn-008bbf28) 範囲 `[['008bbf28', '008bbf2b']]`
  - `FALL_THROUGH` [`008bbf28`](#insn-008bbf28) → [`008bbf2c`](#insn-008bbf2c)
- ブロック [`008bbf2c`](#insn-008bbf2c) 範囲 `[['008bbf2c', '008bbf2f']]`
  - `FALL_THROUGH` [`008bbf2c`](#insn-008bbf2c) → [`008bbf30`](#insn-008bbf30)
- ブロック [`008bbf30`](#insn-008bbf30) 範囲 `[['008bbf30', '008bbf33']]`
  - `FALL_THROUGH` [`008bbf30`](#insn-008bbf30) → [`008bbf34`](#insn-008bbf34)
- ブロック [`008bbf34`](#insn-008bbf34) 範囲 `[['008bbf34', '008bbf37']]`
  - `FALL_THROUGH` [`008bbf34`](#insn-008bbf34) → [`008bbf38`](#insn-008bbf38)
- ブロック [`008bbf38`](#insn-008bbf38) 範囲 `[['008bbf38', '008bbf3f']]`
  - `FALL_THROUGH` [`008bbf3c`](#insn-008bbf3c) → [`008bbf40`](#insn-008bbf40)
- ブロック [`008bbf40`](#insn-008bbf40) 範囲 `[['008bbf40', '008bbf43']]`
  - `FALL_THROUGH` [`008bbf40`](#insn-008bbf40) → [`008bbf44`](#insn-008bbf44)
- ブロック [`008bbf44`](#insn-008bbf44) 範囲 `[['008bbf44', '008bbf47']]`
  - `UNCONDITIONAL_JUMP` [`008bbf44`](#insn-008bbf44) → [`008bbdb8`](#insn-008bbdb8)
- ブロック [`008bbf48`](#insn-008bbf48) 範囲 `[['008bbf48', '008bbf4b']]`
  - `FALL_THROUGH` [`008bbf48`](#insn-008bbf48) → [`008bbf4c`](#insn-008bbf4c)
- ブロック [`008bbf4c`](#insn-008bbf4c) 範囲 `[['008bbf4c', '008bbf4f']]`
  - `FALL_THROUGH` [`008bbf4c`](#insn-008bbf4c) → [`008bbf50`](#insn-008bbf50)
- ブロック [`008bbf50`](#insn-008bbf50) 範囲 `[['008bbf50', '008bbf5f']]`
  - `FALL_THROUGH` [`008bbf5c`](#insn-008bbf5c) → [`008bbf60`](#insn-008bbf60)
- ブロック [`008bbf60`](#insn-008bbf60) 範囲 `[['008bbf60', '008bbf63']]`
  - `FALL_THROUGH` [`008bbf60`](#insn-008bbf60) → [`008bbf64`](#insn-008bbf64)
- ブロック [`008bbf64`](#insn-008bbf64) 範囲 `[['008bbf64', '008bbf67']]`
  - `FALL_THROUGH` [`008bbf64`](#insn-008bbf64) → [`008bbf68`](#insn-008bbf68)
- ブロック [`008bbf68`](#insn-008bbf68) 範囲 `[['008bbf68', '008bbf6b']]`
  - `FALL_THROUGH` [`008bbf68`](#insn-008bbf68) → [`008bbf6c`](#insn-008bbf6c)
- ブロック [`008bbf6c`](#insn-008bbf6c) 範囲 `[['008bbf6c', '008bbf73']]`
  - `FALL_THROUGH` [`008bbf70`](#insn-008bbf70) → [`008bbf74`](#insn-008bbf74)
- ブロック [`008bbf74`](#insn-008bbf74) 範囲 `[['008bbf74', '008bbf77']]`
  - `CONDITIONAL_JUMP` [`008bbf74`](#insn-008bbf74) → [`008bbf80`](#insn-008bbf80)
  - `FALL_THROUGH` [`008bbf74`](#insn-008bbf74) → [`008bbf78`](#insn-008bbf78)
- ブロック [`008bbf78`](#insn-008bbf78) 範囲 `[['008bbf78', '008bbf7b']]`
  - `FALL_THROUGH` [`008bbf78`](#insn-008bbf78) → [`008bbf7c`](#insn-008bbf7c)
- ブロック [`008bbf7c`](#insn-008bbf7c) 範囲 `[['008bbf7c', '008bbf7f']]`
  - `FALL_THROUGH` [`008bbf7c`](#insn-008bbf7c) → [`008bbf80`](#insn-008bbf80)
- ブロック [`008bbf80`](#insn-008bbf80) 範囲 `[['008bbf80', '008bbf83']]`
  - `FALL_THROUGH` [`008bbf80`](#insn-008bbf80) → [`008bbf84`](#insn-008bbf84)
- ブロック [`008bbf84`](#insn-008bbf84) 範囲 `[['008bbf84', '008bbf87']]`
  - `CONDITIONAL_JUMP` [`008bbf84`](#insn-008bbf84) → [`008bbff4`](#insn-008bbff4)
  - `FALL_THROUGH` [`008bbf84`](#insn-008bbf84) → [`008bbf88`](#insn-008bbf88)
- ブロック [`008bbf88`](#insn-008bbf88) 範囲 `[['008bbf88', '008bbf8b']]`
  - `FALL_THROUGH` [`008bbf88`](#insn-008bbf88) → [`008bbf8c`](#insn-008bbf8c)
- ブロック [`008bbf8c`](#insn-008bbf8c) 範囲 `[['008bbf8c', '008bbf8f']]`
  - `FALL_THROUGH` [`008bbf8c`](#insn-008bbf8c) → [`008bbf90`](#insn-008bbf90)
- ブロック [`008bbf90`](#insn-008bbf90) 範囲 `[['008bbf90', '008bbf93']]`
  - `FALL_THROUGH` [`008bbf90`](#insn-008bbf90) → [`008bbf94`](#insn-008bbf94)
- ブロック [`008bbf94`](#insn-008bbf94) 範囲 `[['008bbf94', '008bbf97']]`
  - `FALL_THROUGH` [`008bbf94`](#insn-008bbf94) → [`008bbf98`](#insn-008bbf98)
- ブロック [`008bbf98`](#insn-008bbf98) 範囲 `[['008bbf98', '008bbf9b']]`
  - `FALL_THROUGH` [`008bbf98`](#insn-008bbf98) → [`008bbf9c`](#insn-008bbf9c)
- ブロック [`008bbf9c`](#insn-008bbf9c) 範囲 `[['008bbf9c', '008bbf9f']]`
  - `FALL_THROUGH` [`008bbf9c`](#insn-008bbf9c) → [`008bbfa0`](#insn-008bbfa0)
- ブロック [`008bbfa0`](#insn-008bbfa0) 範囲 `[['008bbfa0', '008bbfa3']]`
  - `FALL_THROUGH` [`008bbfa0`](#insn-008bbfa0) → [`008bbfa4`](#insn-008bbfa4)
- ブロック [`008bbfa4`](#insn-008bbfa4) 範囲 `[['008bbfa4', '008bbfa7']]`
  - `FALL_THROUGH` [`008bbfa4`](#insn-008bbfa4) → [`008bbfa8`](#insn-008bbfa8)
- ブロック [`008bbfa8`](#insn-008bbfa8) 範囲 `[['008bbfa8', '008bbfab']]`
  - `FALL_THROUGH` [`008bbfa8`](#insn-008bbfa8) → [`008bbfac`](#insn-008bbfac)
- ブロック [`008bbfac`](#insn-008bbfac) 範囲 `[['008bbfac', '008bbfaf']]`
  - `FALL_THROUGH` [`008bbfac`](#insn-008bbfac) → [`008bbfb0`](#insn-008bbfb0)
- ブロック [`008bbfb0`](#insn-008bbfb0) 範囲 `[['008bbfb0', '008bbfb3']]`
  - `FALL_THROUGH` [`008bbfb0`](#insn-008bbfb0) → [`008bbfb4`](#insn-008bbfb4)
- ブロック [`008bbfb4`](#insn-008bbfb4) 範囲 `[['008bbfb4', '008bbfb7']]`
  - `FALL_THROUGH` [`008bbfb4`](#insn-008bbfb4) → [`008bbfb8`](#insn-008bbfb8)
- ブロック [`008bbfb8`](#insn-008bbfb8) 範囲 `[['008bbfb8', '008bbfbb']]`
  - `UNCONDITIONAL_JUMP` [`008bbfb8`](#insn-008bbfb8) → [`008bbff4`](#insn-008bbff4)
- ブロック [`008bbfbc`](#insn-008bbfbc) 範囲 `[['008bbfbc', '008bbfbf']]`
  - `FALL_THROUGH` [`008bbfbc`](#insn-008bbfbc) → [`008bbfc0`](#insn-008bbfc0)
- ブロック [`008bbfc0`](#insn-008bbfc0) 範囲 `[['008bbfc0', '008bbfc3']]`
  - `FALL_THROUGH` [`008bbfc0`](#insn-008bbfc0) → [`008bbfc4`](#insn-008bbfc4)
- ブロック [`008bbfc4`](#insn-008bbfc4) 範囲 `[['008bbfc4', '008bbfc7']]`
  - `FALL_THROUGH` [`008bbfc4`](#insn-008bbfc4) → [`008bbfc8`](#insn-008bbfc8)
- ブロック [`008bbfc8`](#insn-008bbfc8) 範囲 `[['008bbfc8', '008bbfcf']]`
  - `FALL_THROUGH` [`008bbfcc`](#insn-008bbfcc) → [`008bbfd0`](#insn-008bbfd0)
- ブロック [`008bbfd0`](#insn-008bbfd0) 範囲 `[['008bbfd0', '008bbfd3']]`
  - `FALL_THROUGH` [`008bbfd0`](#insn-008bbfd0) → [`008bbfd4`](#insn-008bbfd4)
- ブロック [`008bbfd4`](#insn-008bbfd4) 範囲 `[['008bbfd4', '008bbfdb']]`
  - `FALL_THROUGH` [`008bbfd8`](#insn-008bbfd8) → [`008bbfdc`](#insn-008bbfdc)
- ブロック [`008bbfdc`](#insn-008bbfdc) 範囲 `[['008bbfdc', '008bbfdf']]`
  - `FALL_THROUGH` [`008bbfdc`](#insn-008bbfdc) → [`008bbfe0`](#insn-008bbfe0)
- ブロック [`008bbfe0`](#insn-008bbfe0) 範囲 `[['008bbfe0', '008bbfe3']]`
  - `FALL_THROUGH` [`008bbfe0`](#insn-008bbfe0) → [`008bbfe4`](#insn-008bbfe4)
- ブロック [`008bbfe4`](#insn-008bbfe4) 範囲 `[['008bbfe4', '008bbfe7']]`
  - `CONDITIONAL_JUMP` [`008bbfe4`](#insn-008bbfe4) → [`008bbff0`](#insn-008bbff0)
  - `FALL_THROUGH` [`008bbfe4`](#insn-008bbfe4) → [`008bbfe8`](#insn-008bbfe8)
- ブロック [`008bbfe8`](#insn-008bbfe8) 範囲 `[['008bbfe8', '008bbfeb']]`
  - `FALL_THROUGH` [`008bbfe8`](#insn-008bbfe8) → [`008bbfec`](#insn-008bbfec)
- ブロック [`008bbfec`](#insn-008bbfec) 範囲 `[['008bbfec', '008bbfef']]`
  - `FALL_THROUGH` [`008bbfec`](#insn-008bbfec) → [`008bbff0`](#insn-008bbff0)
- ブロック [`008bbff0`](#insn-008bbff0) 範囲 `[['008bbff0', '008bbff3']]`
  - `FALL_THROUGH` [`008bbff0`](#insn-008bbff0) → [`008bbff4`](#insn-008bbff4)
- ブロック [`008bbff4`](#insn-008bbff4) 範囲 `[['008bbff4', '008bbff7']]`
  - `FALL_THROUGH` [`008bbff4`](#insn-008bbff4) → [`008bbff8`](#insn-008bbff8)
- ブロック [`008bbff8`](#insn-008bbff8) 範囲 `[['008bbff8', '008bbffb']]`
  - `FALL_THROUGH` [`008bbff8`](#insn-008bbff8) → [`008bbffc`](#insn-008bbffc)
- ブロック [`008bbffc`](#insn-008bbffc) 範囲 `[['008bbffc', '008bbfff']]`
  - `FALL_THROUGH` [`008bbffc`](#insn-008bbffc) → [`008bc000`](#insn-008bc000)
- ブロック [`008bc000`](#insn-008bc000) 範囲 `[['008bc000', '008bc003']]`
  - `CONDITIONAL_JUMP` [`008bc000`](#insn-008bc000) → [`008bc0ec`](#insn-008bc0ec)
  - `FALL_THROUGH` [`008bc000`](#insn-008bc000) → [`008bc004`](#insn-008bc004)
- ブロック [`008bc004`](#insn-008bc004) 範囲 `[['008bc004', '008bc007']]`
  - `FALL_THROUGH` [`008bc004`](#insn-008bc004) → [`008bc008`](#insn-008bc008)
- ブロック [`008bc008`](#insn-008bc008) 範囲 `[['008bc008', '008bc00b']]`
  - `FALL_THROUGH` [`008bc008`](#insn-008bc008) → [`008bc00c`](#insn-008bc00c)
- ブロック [`008bc00c`](#insn-008bc00c) 範囲 `[['008bc00c', '008bc00f']]`
  - `FALL_THROUGH` [`008bc00c`](#insn-008bc00c) → [`008bc010`](#insn-008bc010)
- ブロック [`008bc010`](#insn-008bc010) 範囲 `[['008bc010', '008bc013']]`
  - `FALL_THROUGH` [`008bc010`](#insn-008bc010) → [`008bc014`](#insn-008bc014)
- ブロック [`008bc014`](#insn-008bc014) 範囲 `[['008bc014', '008bc017']]`
  - `FALL_THROUGH` [`008bc014`](#insn-008bc014) → [`008bc018`](#insn-008bc018)
- ブロック [`008bc018`](#insn-008bc018) 範囲 `[['008bc018', '008bc01b']]`
  - `FALL_THROUGH` [`008bc018`](#insn-008bc018) → [`008bc01c`](#insn-008bc01c)
- ブロック [`008bc01c`](#insn-008bc01c) 範囲 `[['008bc01c', '008bc01f']]`
  - `FALL_THROUGH` [`008bc01c`](#insn-008bc01c) → [`008bc020`](#insn-008bc020)
- ブロック [`008bc020`](#insn-008bc020) 範囲 `[['008bc020', '008bc023']]`
  - `FALL_THROUGH` [`008bc020`](#insn-008bc020) → [`008bc024`](#insn-008bc024)
- ブロック [`008bc024`](#insn-008bc024) 範囲 `[['008bc024', '008bc027']]`
- ブロック [`008bc028`](#insn-008bc028) 範囲 `[['008bc028', '008bc02b']]`
  - `FALL_THROUGH` [`008bc028`](#insn-008bc028) → [`008bc02c`](#insn-008bc02c)
- ブロック [`008bc02c`](#insn-008bc02c) 範囲 `[['008bc02c', '008bc02f']]`
  - `FALL_THROUGH` [`008bc02c`](#insn-008bc02c) → [`008bc030`](#insn-008bc030)
- ブロック [`008bc030`](#insn-008bc030) 範囲 `[['008bc030', '008bc033']]`
  - `FALL_THROUGH` [`008bc030`](#insn-008bc030) → [`008bc034`](#insn-008bc034)
- ブロック [`008bc034`](#insn-008bc034) 範囲 `[['008bc034', '008bc037']]`
  - `CONDITIONAL_JUMP` [`008bc034`](#insn-008bc034) → [`008bc0ec`](#insn-008bc0ec)
  - `FALL_THROUGH` [`008bc034`](#insn-008bc034) → [`008bc038`](#insn-008bc038)
- ブロック [`008bc038`](#insn-008bc038) 範囲 `[['008bc038', '008bc03b']]`
- ブロック [`008bc03c`](#insn-008bc03c) 範囲 `[['008bc03c', '008bc03f']]`
  - `FALL_THROUGH` [`008bc03c`](#insn-008bc03c) → [`008bc040`](#insn-008bc040)
- ブロック [`008bc040`](#insn-008bc040) 範囲 `[['008bc040', '008bc043']]`
  - `FALL_THROUGH` [`008bc040`](#insn-008bc040) → [`008bc044`](#insn-008bc044)
- ブロック [`008bc044`](#insn-008bc044) 範囲 `[['008bc044', '008bc04f']]`
  - `CONDITIONAL_JUMP` [`008bc04c`](#insn-008bc04c) → [`008bc0ec`](#insn-008bc0ec)
  - `FALL_THROUGH` [`008bc04c`](#insn-008bc04c) → [`008bc050`](#insn-008bc050)
- ブロック [`008bc050`](#insn-008bc050) 範囲 `[['008bc050', '008bc053']]`
  - `FALL_THROUGH` [`008bc050`](#insn-008bc050) → [`008bc054`](#insn-008bc054)
- ブロック [`008bc054`](#insn-008bc054) 範囲 `[['008bc054', '008bc057']]`
  - `FALL_THROUGH` [`008bc054`](#insn-008bc054) → [`008bc058`](#insn-008bc058)
- ブロック [`008bc058`](#insn-008bc058) 範囲 `[['008bc058', '008bc05b']]`
  - `UNCONDITIONAL_JUMP` [`008bc058`](#insn-008bc058) → [`008bc094`](#insn-008bc094)
- ブロック [`008bc094`](#insn-008bc094) 範囲 `[['008bc094', '008bc0a3']]`
  - `CONDITIONAL_JUMP` [`008bc0a0`](#insn-008bc0a0) → [`008bc0b0`](#insn-008bc0b0)
  - `FALL_THROUGH` [`008bc0a0`](#insn-008bc0a0) → [`008bc0a4`](#insn-008bc0a4)
- ブロック [`008bc0a4`](#insn-008bc0a4) 範囲 `[['008bc0a4', '008bc0af']]`
  - `UNCONDITIONAL_JUMP` [`008bc0ac`](#insn-008bc0ac) → [`008bc0b8`](#insn-008bc0b8)
- ブロック [`008bc0b0`](#insn-008bc0b0) 範囲 `[['008bc0b0', '008bc0b3']]`
  - `CONDITIONAL_JUMP` [`008bc0b0`](#insn-008bc0b0) → [`008bc0cc`](#insn-008bc0cc)
  - `FALL_THROUGH` [`008bc0b0`](#insn-008bc0b0) → [`008bc0b4`](#insn-008bc0b4)
- ブロック [`008bc0b4`](#insn-008bc0b4) 範囲 `[['008bc0b4', '008bc0b7']]`
  - `FALL_THROUGH` [`008bc0b4`](#insn-008bc0b4) → [`008bc0b8`](#insn-008bc0b8)
- ブロック [`008bc0b8`](#insn-008bc0b8) 範囲 `[['008bc0b8', '008bc0c7']]`
  - `UNCONDITIONAL_JUMP` [`008bc0c4`](#insn-008bc0c4) → [`008bc0cc`](#insn-008bc0cc)
- ブロック [`008bc0cc`](#insn-008bc0cc) 範囲 `[['008bc0cc', '008bc0d3']]`
  - `FALL_THROUGH` [`008bc0d0`](#insn-008bc0d0) → [`008bc0d4`](#insn-008bc0d4)
- ブロック [`008bc0d4`](#insn-008bc0d4) 範囲 `[['008bc0d4', '008bc0e3']]`
  - `CONDITIONAL_JUMP` [`008bc0e0`](#insn-008bc0e0) → [`008bc0ec`](#insn-008bc0ec)
  - `FALL_THROUGH` [`008bc0e0`](#insn-008bc0e0) → [`008bc0e4`](#insn-008bc0e4)
- ブロック [`008bc0e4`](#insn-008bc0e4) 範囲 `[['008bc0e4', '008bc0eb']]`
- ブロック [`008bc0ec`](#insn-008bc0ec) 範囲 `[['008bc0ec', '008bc0ef']]`

## 命令位置別の参照

- [`008bbcd0`](#insn-008bbcd0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbcd4`](#insn-008bbcd4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbcd8`](#insn-008bbcd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbcdc`](#insn-008bbcdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbce0`](#insn-008bbce0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbce4`](#insn-008bbce4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbd10`](#insn-008bbd10) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbd14`](#insn-008bbd14) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`008bbd20`](#insn-008bbd20) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbd4c`](#insn-008bbd4c) → [`008bbd70`](#insn-008bbd70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbd54`](#insn-008bbd54) → [`008bbd78`](#insn-008bbd78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbd64`](#insn-008bbd64) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbd68`](#insn-008bbd68) → [`008bbd9c`](#insn-008bbd9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbd6c`](#insn-008bbd6c) → [`008bbdb4`](#insn-008bbdb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbd70`](#insn-008bbd70) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbd74`](#insn-008bbd74) → [`008bbdb4`](#insn-008bbdb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbd80`](#insn-008bbd80) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbd94`](#insn-008bbd94) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbd98`](#insn-008bbd98) → [`008bbdb4`](#insn-008bbdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbda4`](#insn-008bbda4) → [`008bbf28`](#insn-008bbf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbda8`](#insn-008bbda8) → `Stack[-0xd0]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbdb4`](#insn-008bbdb4) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbddc`](#insn-008bbddc) → [`008b9358`](../008b9/008b9358.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b9358` · 推定シンボル `None` · 推定型 `None`
- [`008bbde0`](#insn-008bbde0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbde8`](#insn-008bbde8) → [`008bbdf8`](#insn-008bbdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbdec`](#insn-008bbdec) → [`008bbe0c`](#insn-008bbe0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbdf4`](#insn-008bbdf4) → [`008bbe00`](#insn-008bbe00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe00`](#insn-008bbe00) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe0c`](#insn-008bbe0c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe18`](#insn-008bbe18) → [`008bbe28`](#insn-008bbe28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe1c`](#insn-008bbe1c) → [`008bbe3c`](#insn-008bbe3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe24`](#insn-008bbe24) → [`008bbe30`](#insn-008bbe30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe30`](#insn-008bbe30) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe40`](#insn-008bbe40) → [`008bbe64`](#insn-008bbe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe4c`](#insn-008bbe4c) → [`008bbe64`](#insn-008bbe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe58`](#insn-008bbe58) → [`008bbed0`](#insn-008bbed0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe60`](#insn-008bbe60) → [`008bbff0`](#insn-008bbff0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe6c`](#insn-008bbe6c) → [`008bbe7c`](#insn-008bbe7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe70`](#insn-008bbe70) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe78`](#insn-008bbe78) → [`008bbf80`](#insn-008bbf80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbe90`](#insn-008bbe90) → [`008bc03c`](#insn-008bc03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbeb4`](#insn-008bbeb4) → [`008bbf48`](#insn-008bbf48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbebc`](#insn-008bbebc) → [`008bc028`](#insn-008bc028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbec4`](#insn-008bbec4) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`008bbecc`](#insn-008bbecc) → [`008bbf4c`](#insn-008bbf4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbee8`](#insn-008bbee8) → [`008bc040`](#insn-008bc040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbf0c`](#insn-008bbf0c) → [`008bbfbc`](#insn-008bbfbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbf14`](#insn-008bbf14) → [`008bc028`](#insn-008bc028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbf1c`](#insn-008bbf1c) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`008bbf24`](#insn-008bbf24) → [`008bbfc0`](#insn-008bbfc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbf2c`](#insn-008bbf2c) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbf30`](#insn-008bbf30) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbf44`](#insn-008bbf44) → [`008bbdb8`](#insn-008bbdb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbf60`](#insn-008bbf60) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbf68`](#insn-008bbf68) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`008bbf74`](#insn-008bbf74) → [`008bbf80`](#insn-008bbf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbf7c`](#insn-008bbf7c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`008bbf84`](#insn-008bbf84) → [`008bbff4`](#insn-008bbff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbf88`](#insn-008bbf88) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`008bbf94`](#insn-008bbf94) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`008bbfa0`](#insn-008bbfa0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`008bbfac`](#insn-008bbfac) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`008bbfb8`](#insn-008bbfb8) → [`008bbff4`](#insn-008bbff4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbfd8`](#insn-008bbfd8) → [`00c590a0`](../00c59/00c590a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590a0` · 推定シンボル `None` · 推定型 `None`
- [`008bbfe4`](#insn-008bbfe4) → [`008bbff0`](#insn-008bbff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bbfec`](#insn-008bbfec) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`008bbff8`](#insn-008bbff8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc000`](#insn-008bc000) → [`008bc0ec`](#insn-008bc0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc008`](#insn-008bc008) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc00c`](#insn-008bc00c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc010`](#insn-008bc010) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc014`](#insn-008bc014) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc018`](#insn-008bc018) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc01c`](#insn-008bc01c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc02c`](#insn-008bc02c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc034`](#insn-008bc034) → [`008bc0ec`](#insn-008bc0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc038`](#insn-008bc038) → [`00441220`](../00441/00441220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00441220` · 推定シンボル `None` · 推定型 `None`
- [`008bc044`](#insn-008bc044) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc04c`](#insn-008bc04c) → [`008bc0ec`](#insn-008bc0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc050`](#insn-008bc050) → [`008bd514`](../008bd/008bd514.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bd514` · 推定シンボル `None` · 推定型 `None`
- [`008bc058`](#insn-008bc058) → [`008bc094`](#insn-008bc094) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc094`](#insn-008bc094) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc0a0`](#insn-008bc0a0) → [`008bc0b0`](#insn-008bc0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc0ac`](#insn-008bc0ac) → [`008bc0b8`](#insn-008bc0b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc0b0`](#insn-008bc0b0) → [`008bc0cc`](#insn-008bc0cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc0b8`](#insn-008bc0b8) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc0c4`](#insn-008bc0c4) → [`008bc0cc`](#insn-008bc0cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc0d0`](#insn-008bc0d0) → [`008bbc90`](008bbc90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008bbc90` · 推定シンボル `None` · 推定型 `None`
- [`008bc0d8`](#insn-008bc0d8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc0e0`](#insn-008bc0e0) → [`008bc0ec`](#insn-008bc0ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`008bc0e8`](#insn-008bc0e8) → [`00c54fec`](../00c54/00c54fec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54fec` · 推定シンボル `None` · 推定型 `None`
- [`008bc0ec`](#insn-008bc0ec) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`008bbcd0`](#insn-008bbcd0)

~~~json
{
  "source": "008bbcd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbcd4`](#insn-008bbcd4)

~~~json
{
  "source": "008bbcd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbcd8`](#insn-008bbcd8)

~~~json
{
  "source": "008bbcd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbcdc`](#insn-008bbcdc)

~~~json
{
  "source": "008bbcdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbce0`](#insn-008bbce0)

~~~json
{
  "source": "008bbce0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbce4`](#insn-008bbce4)

~~~json
{
  "source": "008bbce4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbd10`](#insn-008bbd10)

~~~json
{
  "source": "008bbd10",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbd14`](#insn-008bbd14)

~~~json
{
  "source": "008bbd14",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bbd20`](#insn-008bbd20)

~~~json
{
  "source": "008bbd20",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbd4c`](#insn-008bbd4c)

~~~json
{
  "source": "008bbd4c",
  "target": "008bbd70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbd54`](#insn-008bbd54)

~~~json
{
  "source": "008bbd54",
  "target": "008bbd78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbd64`](#insn-008bbd64)

~~~json
{
  "source": "008bbd64",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbd68`](#insn-008bbd68)

~~~json
{
  "source": "008bbd68",
  "target": "008bbd9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbd6c`](#insn-008bbd6c)

~~~json
{
  "source": "008bbd6c",
  "target": "008bbdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbd70`](#insn-008bbd70)

~~~json
{
  "source": "008bbd70",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbd74`](#insn-008bbd74)

~~~json
{
  "source": "008bbd74",
  "target": "008bbdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbd80`](#insn-008bbd80)

~~~json
{
  "source": "008bbd80",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbd94`](#insn-008bbd94)

~~~json
{
  "source": "008bbd94",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbd98`](#insn-008bbd98)

~~~json
{
  "source": "008bbd98",
  "target": "008bbdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbda4`](#insn-008bbda4)

~~~json
{
  "source": "008bbda4",
  "target": "008bbf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbda8`](#insn-008bbda8)

~~~json
{
  "source": "008bbda8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbdb4`](#insn-008bbdb4)

~~~json
{
  "source": "008bbdb4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbddc`](#insn-008bbddc)

~~~json
{
  "source": "008bbddc",
  "target": "008b9358",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bbde0`](#insn-008bbde0)

~~~json
{
  "source": "008bbde0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbde8`](#insn-008bbde8)

~~~json
{
  "source": "008bbde8",
  "target": "008bbdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbdec`](#insn-008bbdec)

~~~json
{
  "source": "008bbdec",
  "target": "008bbe0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbdf4`](#insn-008bbdf4)

~~~json
{
  "source": "008bbdf4",
  "target": "008bbe00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe00`](#insn-008bbe00)

~~~json
{
  "source": "008bbe00",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe0c`](#insn-008bbe0c)

~~~json
{
  "source": "008bbe0c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe18`](#insn-008bbe18)

~~~json
{
  "source": "008bbe18",
  "target": "008bbe28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe1c`](#insn-008bbe1c)

~~~json
{
  "source": "008bbe1c",
  "target": "008bbe3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe24`](#insn-008bbe24)

~~~json
{
  "source": "008bbe24",
  "target": "008bbe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe30`](#insn-008bbe30)

~~~json
{
  "source": "008bbe30",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe40`](#insn-008bbe40)

~~~json
{
  "source": "008bbe40",
  "target": "008bbe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe4c`](#insn-008bbe4c)

~~~json
{
  "source": "008bbe4c",
  "target": "008bbe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe58`](#insn-008bbe58)

~~~json
{
  "source": "008bbe58",
  "target": "008bbed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe60`](#insn-008bbe60)

~~~json
{
  "source": "008bbe60",
  "target": "008bbff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe6c`](#insn-008bbe6c)

~~~json
{
  "source": "008bbe6c",
  "target": "008bbe7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe70`](#insn-008bbe70)

~~~json
{
  "source": "008bbe70",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe78`](#insn-008bbe78)

~~~json
{
  "source": "008bbe78",
  "target": "008bbf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbe90`](#insn-008bbe90)

~~~json
{
  "source": "008bbe90",
  "target": "008bc03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbeb4`](#insn-008bbeb4)

~~~json
{
  "source": "008bbeb4",
  "target": "008bbf48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbebc`](#insn-008bbebc)

~~~json
{
  "source": "008bbebc",
  "target": "008bc028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbec4`](#insn-008bbec4)

~~~json
{
  "source": "008bbec4",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bbecc`](#insn-008bbecc)

~~~json
{
  "source": "008bbecc",
  "target": "008bbf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbee8`](#insn-008bbee8)

~~~json
{
  "source": "008bbee8",
  "target": "008bc040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbf0c`](#insn-008bbf0c)

~~~json
{
  "source": "008bbf0c",
  "target": "008bbfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbf14`](#insn-008bbf14)

~~~json
{
  "source": "008bbf14",
  "target": "008bc028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbf1c`](#insn-008bbf1c)

~~~json
{
  "source": "008bbf1c",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bbf24`](#insn-008bbf24)

~~~json
{
  "source": "008bbf24",
  "target": "008bbfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbf2c`](#insn-008bbf2c)

~~~json
{
  "source": "008bbf2c",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbf30`](#insn-008bbf30)

~~~json
{
  "source": "008bbf30",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbf44`](#insn-008bbf44)

~~~json
{
  "source": "008bbf44",
  "target": "008bbdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbf60`](#insn-008bbf60)

~~~json
{
  "source": "008bbf60",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbf68`](#insn-008bbf68)

~~~json
{
  "source": "008bbf68",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bbf74`](#insn-008bbf74)

~~~json
{
  "source": "008bbf74",
  "target": "008bbf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbf7c`](#insn-008bbf7c)

~~~json
{
  "source": "008bbf7c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bbf84`](#insn-008bbf84)

~~~json
{
  "source": "008bbf84",
  "target": "008bbff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbf88`](#insn-008bbf88)

~~~json
{
  "source": "008bbf88",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bbf94`](#insn-008bbf94)

~~~json
{
  "source": "008bbf94",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bbfa0`](#insn-008bbfa0)

~~~json
{
  "source": "008bbfa0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bbfac`](#insn-008bbfac)

~~~json
{
  "source": "008bbfac",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bbfb8`](#insn-008bbfb8)

~~~json
{
  "source": "008bbfb8",
  "target": "008bbff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbfd8`](#insn-008bbfd8)

~~~json
{
  "source": "008bbfd8",
  "target": "00c590a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bbfe4`](#insn-008bbfe4)

~~~json
{
  "source": "008bbfe4",
  "target": "008bbff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bbfec`](#insn-008bbfec)

~~~json
{
  "source": "008bbfec",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bbff8`](#insn-008bbff8)

~~~json
{
  "source": "008bbff8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc000`](#insn-008bc000)

~~~json
{
  "source": "008bc000",
  "target": "008bc0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc008`](#insn-008bc008)

~~~json
{
  "source": "008bc008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc00c`](#insn-008bc00c)

~~~json
{
  "source": "008bc00c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc010`](#insn-008bc010)

~~~json
{
  "source": "008bc010",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc014`](#insn-008bc014)

~~~json
{
  "source": "008bc014",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc018`](#insn-008bc018)

~~~json
{
  "source": "008bc018",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc01c`](#insn-008bc01c)

~~~json
{
  "source": "008bc01c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc02c`](#insn-008bc02c)

~~~json
{
  "source": "008bc02c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc034`](#insn-008bc034)

~~~json
{
  "source": "008bc034",
  "target": "008bc0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc038`](#insn-008bc038)

~~~json
{
  "source": "008bc038",
  "target": "00441220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bc044`](#insn-008bc044)

~~~json
{
  "source": "008bc044",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc04c`](#insn-008bc04c)

~~~json
{
  "source": "008bc04c",
  "target": "008bc0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc050`](#insn-008bc050)

~~~json
{
  "source": "008bc050",
  "target": "008bd514",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bc058`](#insn-008bc058)

~~~json
{
  "source": "008bc058",
  "target": "008bc094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc094`](#insn-008bc094)

~~~json
{
  "source": "008bc094",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc0a0`](#insn-008bc0a0)

~~~json
{
  "source": "008bc0a0",
  "target": "008bc0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc0ac`](#insn-008bc0ac)

~~~json
{
  "source": "008bc0ac",
  "target": "008bc0b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc0b0`](#insn-008bc0b0)

~~~json
{
  "source": "008bc0b0",
  "target": "008bc0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc0b8`](#insn-008bc0b8)

~~~json
{
  "source": "008bc0b8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc0c4`](#insn-008bc0c4)

~~~json
{
  "source": "008bc0c4",
  "target": "008bc0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc0d0`](#insn-008bc0d0)

~~~json
{
  "source": "008bc0d0",
  "target": "008bbc90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bc0d8`](#insn-008bc0d8)

~~~json
{
  "source": "008bc0d8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc0e0`](#insn-008bc0e0)

~~~json
{
  "source": "008bc0e0",
  "target": "008bc0ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`008bc0e8`](#insn-008bc0e8)

~~~json
{
  "source": "008bc0e8",
  "target": "00c54fec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`008bc0ec`](#insn-008bc0ec)

~~~json
{
  "source": "008bc0ec",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
