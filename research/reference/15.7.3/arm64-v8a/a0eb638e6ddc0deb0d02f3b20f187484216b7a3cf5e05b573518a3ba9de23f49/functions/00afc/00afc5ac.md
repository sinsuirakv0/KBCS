# 00afc5ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afc4e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afc/00afc4e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0063.md#compare-980b133a11c4546c0895bac50922b1d1)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afc5f0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc5f0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-5947e5a9c897cdafc4a23e833f46b19a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afc5ac",
  "name": "_ZN8firebase15CleanupNotifierD2Ev",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f201b12abb428f434dd0150311560e22a5d990dfa2227484dc6bc45e9602aa2d",
  "source_text_sha256": "f201b12abb428f434dd0150311560e22a5d990dfa2227484dc6bc45e9602aa2d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afc5ac",
        "00afc693"
      ]
    ],
    "bytes_sha256": "91b0751aa613d288c9f0751cee13f61d27ca4d830641c5fe1abb509cfe1075b6",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bddd80](../00bdd/00bddd80.md)

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bddc00](../00bdd/00bddc00.md)
- [00bddd60](../00bdd/00bddd60.md)
- [00bdeca0](../00bde/00bdeca0.md)
- [00bdecb0](../00bde/00bdecb0.md)
- [00bdecc0](../00bde/00bdecc0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2275 bytes

~~~c

void _ZN8firebase15CleanupNotifierD2Ev(long param_1)

{
  undefined *puVar1;
  long lVar2;
  undefined8 uVar3;
  void *pvVar4;
  
  _ZN8firebase5Mutex7AcquireEv();
                    /* try { // try from 00afc5c8 to 00bfc5d3 has its CatchHandler @ 00b003a0 */
  if (*(char *)(param_1 + 0x40) == '\0') {
    lVar2 = *(long *)(param_1 + 0x28);
    while (lVar2 != param_1 + 0x30) {
      uVar3 = *(undefined8 *)(lVar2 + 0x20);
      (**(code **)(lVar2 + 0x28))(uVar3);
      _ZN8firebase15CleanupNotifier16UnregisterObjectEPv(param_1,uVar3);
      lVar2 = *(long *)(param_1 + 0x28);
                    /* try { // try from 00afc5fc to 00bfc60f has its CatchHandler @ 00b00398 */
    }
    *(undefined1 *)(param_1 + 0x40) = 1;
  }
  _ZN8firebase5Mutex7ReleaseEv(param_1);
                    /* try { // try from 00afc610 to 00bfc61b has its CatchHandler @ 00b00418 */
  _ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv(param_1);
  uVar3 = *(undefined8 *)
           PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b948;
  _ZN8firebase5Mutex7AcquireEv(uVar3);
  puVar1 = PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b940;
  pvVar4 = *(void **)PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c1b940;
  if ((pvVar4 != (void *)0x0) && (*(long *)((long)pvVar4 + 0x10) == 0)) {
                    /* try { // try from 00afc644 to 00bfc667 has its CatchHandler @ 00b00454 */
    _ZNSt6__ndk16__treeINS_12__value_typeIPvPN8firebase15CleanupNotifierEEENS_19__map_value_compareIS2_S6_NS_4lessIS2_EELb1EEENS_9allocatorIS6_EEE7destroyEPNS_11__tree_nodeIS6_S2_EE
              (pvVar4,*(undefined8 *)((long)pvVar4 + 8));
    _ZdlPv(pvVar4);
    *(undefined8 *)puVar1 = 0;
  }
  _ZN8firebase5Mutex7ReleaseEv(uVar3);
  pvVar4 = *(void **)(param_1 + 0x48);
                    /* try { // try from 00afc668 to 00bfc673 has its CatchHandler @ 00b00408 */
  if (pvVar4 != (void *)0x0) {
    *(void **)(param_1 + 0x50) = pvVar4;
    _ZdlPv(pvVar4);
  }
  _ZNSt6__ndk16__treeINS_12__value_typeIPvPFvS2_EEENS_19__map_value_compareIS2_S5_NS_4lessIS2_EELb1EEENS_9allocatorIS5_EEE7destroyEPNS_11__tree_nodeIS5_S2_EE
            (param_1 + 0x28,*(undefined8 *)(param_1 + 0x30));
  _ZN8firebase5MutexD1Ev(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afc5ac"></a> `00afc5ac` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afc5b0"></a> `00afc5b0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc5b4"></a> `00afc5b4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afc5b8"></a> `00afc5b8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00afc5bc"></a> `00afc5bc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afc5c0"></a> `00afc5c0` | `84 85 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afc5c4"></a> `00afc5c4` | `68 02 41 39` | ldrb w8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00afc5c8"></a> `00afc5c8` | `08 02 00 35` | cbnz w8,0x00afc608 | `CONDITIONAL_JUMP`
<a id="insn-00afc5cc"></a> `00afc5cc` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00afc5d0"></a> `00afc5d0` | `75 c2 00 91` | add x21,x19,#0x30 | `FALL_THROUGH`
<a id="insn-00afc5d4"></a> `00afc5d4` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00afc5d8"></a> `00afc5d8` | `40 01 00 54` | b.eq 0x00afc600 | `CONDITIONAL_JUMP`
<a id="insn-00afc5dc"></a> `00afc5dc` | `14 21 42 a9` | ldp x20,x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00afc5e0"></a> `00afc5e0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afc5e4"></a> `00afc5e4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afc5e8"></a> `00afc5e8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afc5ec"></a> `00afc5ec` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00afc5f0"></a> `00afc5f0` | `dc 85 03 94` | bl 0x00bddd60 | `UNCONDITIONAL_CALL`
<a id="insn-00afc5f4"></a> `00afc5f4` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00afc5f8"></a> `00afc5f8` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00afc5fc"></a> `00afc5fc` | `01 ff ff 54` | b.ne 0x00afc5dc | `CONDITIONAL_JUMP`
<a id="insn-00afc600"></a> `00afc600` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afc604"></a> `00afc604` | `68 02 01 39` | strb w8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00afc608"></a> `00afc608` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afc60c"></a> `00afc60c` | `75 85 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afc610"></a> `00afc610` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afc614"></a> `00afc614` | `a3 89 03 94` | bl 0x00bdeca0 | `UNCONDITIONAL_CALL`
<a id="insn-00afc618"></a> `00afc618` | `e8 08 00 f0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afc61c"></a> `00afc61c` | `08 a5 44 f9` | ldr x8,[x8, #0x948] | `FALL_THROUGH`
<a id="insn-00afc620"></a> `00afc620` | `14 01 40 f9` | ldr x20,[x8] | `FALL_THROUGH`
<a id="insn-00afc624"></a> `00afc624` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afc628"></a> `00afc628` | `6a 85 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afc62c"></a> `00afc62c` | `f6 08 00 f0` | adrp x22,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afc630"></a> `00afc630` | `d6 a2 44 f9` | ldr x22,[x22, #0x940] | `FALL_THROUGH`
<a id="insn-00afc634"></a> `00afc634` | `d5 02 40 f9` | ldr x21,[x22] | `FALL_THROUGH`
<a id="insn-00afc638"></a> `00afc638` | `35 01 00 b4` | cbz x21,0x00afc65c | `CONDITIONAL_JUMP`
<a id="insn-00afc63c"></a> `00afc63c` | `a8 0a 40 f9` | ldr x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00afc640"></a> `00afc640` | `e8 00 00 b5` | cbnz x8,0x00afc65c | `CONDITIONAL_JUMP`
<a id="insn-00afc644"></a> `00afc644` | `a1 06 40 f9` | ldr x1,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00afc648"></a> `00afc648` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afc64c"></a> `00afc64c` | `9d 89 03 94` | bl 0x00bdecc0 | `UNCONDITIONAL_CALL`
<a id="insn-00afc650"></a> `00afc650` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afc654"></a> `00afc654` | `6f 7a 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afc658"></a> `00afc658` | `df 02 00 f9` | str xzr,[x22] | `FALL_THROUGH`
<a id="insn-00afc65c"></a> `00afc65c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afc660"></a> `00afc660` | `60 85 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afc664"></a> `00afc664` | `60 26 40 f9` | ldr x0,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00afc668"></a> `00afc668` | `60 00 00 b4` | cbz x0,0x00afc674 | `CONDITIONAL_JUMP`
<a id="insn-00afc66c"></a> `00afc66c` | `60 2a 00 f9` | str x0,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00afc670"></a> `00afc670` | `68 7a 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00afc674"></a> `00afc674` | `61 1a 40 f9` | ldr x1,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00afc678"></a> `00afc678` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00afc67c"></a> `00afc67c` | `8d 89 03 94` | bl 0x00bdecb0 | `UNCONDITIONAL_CALL`
<a id="insn-00afc680"></a> `00afc680` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afc684"></a> `00afc684` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afc688"></a> `00afc688` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afc68c"></a> `00afc68c` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afc690"></a> `00afc690` | `5c 85 03 14` | b 0x00bddc00 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afc5ac`](#insn-00afc5ac) 範囲 `[['00afc5ac', '00afc5c7']]`
  - `FALL_THROUGH` [`00afc5c4`](#insn-00afc5c4) → [`00afc5c8`](#insn-00afc5c8)
- ブロック [`00afc5c8`](#insn-00afc5c8) 範囲 `[['00afc5c8', '00afc5cb']]`
  - `CONDITIONAL_JUMP` [`00afc5c8`](#insn-00afc5c8) → [`00afc608`](#insn-00afc608)
  - `FALL_THROUGH` [`00afc5c8`](#insn-00afc5c8) → [`00afc5cc`](#insn-00afc5cc)
- ブロック [`00afc5cc`](#insn-00afc5cc) 範囲 `[['00afc5cc', '00afc5db']]`
  - `CONDITIONAL_JUMP` [`00afc5d8`](#insn-00afc5d8) → [`00afc600`](#insn-00afc600)
  - `FALL_THROUGH` [`00afc5d8`](#insn-00afc5d8) → [`00afc5dc`](#insn-00afc5dc)
- ブロック [`00afc5dc`](#insn-00afc5dc) 範囲 `[['00afc5dc', '00afc5fb']]`
  - `FALL_THROUGH` [`00afc5f8`](#insn-00afc5f8) → [`00afc5fc`](#insn-00afc5fc)
- ブロック [`00afc5fc`](#insn-00afc5fc) 範囲 `[['00afc5fc', '00afc5ff']]`
  - `CONDITIONAL_JUMP` [`00afc5fc`](#insn-00afc5fc) → [`00afc5dc`](#insn-00afc5dc)
  - `FALL_THROUGH` [`00afc5fc`](#insn-00afc5fc) → [`00afc600`](#insn-00afc600)
- ブロック [`00afc600`](#insn-00afc600) 範囲 `[['00afc600', '00afc607']]`
  - `FALL_THROUGH` [`00afc604`](#insn-00afc604) → [`00afc608`](#insn-00afc608)
- ブロック [`00afc608`](#insn-00afc608) 範囲 `[['00afc608', '00afc60f']]`
  - `FALL_THROUGH` [`00afc60c`](#insn-00afc60c) → [`00afc610`](#insn-00afc610)
- ブロック [`00afc610`](#insn-00afc610) 範囲 `[['00afc610', '00afc63b']]`
  - `CONDITIONAL_JUMP` [`00afc638`](#insn-00afc638) → [`00afc65c`](#insn-00afc65c)
  - `FALL_THROUGH` [`00afc638`](#insn-00afc638) → [`00afc63c`](#insn-00afc63c)
- ブロック [`00afc63c`](#insn-00afc63c) 範囲 `[['00afc63c', '00afc643']]`
  - `CONDITIONAL_JUMP` [`00afc640`](#insn-00afc640) → [`00afc65c`](#insn-00afc65c)
  - `FALL_THROUGH` [`00afc640`](#insn-00afc640) → [`00afc644`](#insn-00afc644)
- ブロック [`00afc644`](#insn-00afc644) 範囲 `[['00afc644', '00afc65b']]`
  - `FALL_THROUGH` [`00afc658`](#insn-00afc658) → [`00afc65c`](#insn-00afc65c)
- ブロック [`00afc65c`](#insn-00afc65c) 範囲 `[['00afc65c', '00afc667']]`
  - `FALL_THROUGH` [`00afc664`](#insn-00afc664) → [`00afc668`](#insn-00afc668)
- ブロック [`00afc668`](#insn-00afc668) 範囲 `[['00afc668', '00afc66b']]`
  - `CONDITIONAL_JUMP` [`00afc668`](#insn-00afc668) → [`00afc674`](#insn-00afc674)
  - `FALL_THROUGH` [`00afc668`](#insn-00afc668) → [`00afc66c`](#insn-00afc66c)
- ブロック [`00afc66c`](#insn-00afc66c) 範囲 `[['00afc66c', '00afc673']]`
  - `FALL_THROUGH` [`00afc670`](#insn-00afc670) → [`00afc674`](#insn-00afc674)
- ブロック [`00afc674`](#insn-00afc674) 範囲 `[['00afc674', '00afc693']]`

## 命令位置別の参照

- [`00afc5ac`](#insn-00afc5ac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc5b0`](#insn-00afc5b0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc5b4`](#insn-00afc5b4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc5c0`](#insn-00afc5c0) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00afc5c8`](#insn-00afc5c8) → [`00afc608`](#insn-00afc608) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc5d8`](#insn-00afc5d8) → [`00afc600`](#insn-00afc600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc5f0`](#insn-00afc5f0) → [`00bddd60`](../00bdd/00bddd60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddd60` · 推定シンボル `None` · 推定型 `None`
- [`00afc5fc`](#insn-00afc5fc) → [`00afc5dc`](#insn-00afc5dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc60c`](#insn-00afc60c) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afc614`](#insn-00afc614) → [`00bdeca0`](../00bde/00bdeca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdeca0` · 推定シンボル `None` · 推定型 `None`
- [`00afc61c`](#insn-00afc61c) → `00c1b948`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afc620`](#insn-00afc620) → `010a0d08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E` · 推定型 `undefined8`
- [`00afc628`](#insn-00afc628) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00afc630`](#insn-00afc630) → `00c1b940`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afc634`](#insn-00afc634) → `010a0d10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E` · 推定型 `undefined8`
- [`00afc638`](#insn-00afc638) → [`00afc65c`](#insn-00afc65c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc640`](#insn-00afc640) → [`00afc65c`](#insn-00afc65c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc64c`](#insn-00afc64c) → [`00bdecc0`](../00bde/00bdecc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdecc0` · 推定シンボル `None` · 推定型 `None`
- [`00afc654`](#insn-00afc654) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afc658`](#insn-00afc658) → `010a0d10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E` · 推定型 `undefined8`
- [`00afc660`](#insn-00afc660) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afc668`](#insn-00afc668) → [`00afc674`](#insn-00afc674) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc670`](#insn-00afc670) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00afc67c`](#insn-00afc67c) → [`00bdecb0`](../00bde/00bdecb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdecb0` · 推定シンボル `None` · 推定型 `None`
- [`00afc684`](#insn-00afc684) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc688`](#insn-00afc688) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afc690`](#insn-00afc690) → [`00bddc00`](../00bdd/00bddc00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc00` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afc5ac`](#insn-00afc5ac)

~~~json
{
  "source": "00afc5ac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc5b0`](#insn-00afc5b0)

~~~json
{
  "source": "00afc5b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc5b4`](#insn-00afc5b4)

~~~json
{
  "source": "00afc5b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc5c0`](#insn-00afc5c0)

~~~json
{
  "source": "00afc5c0",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc5c8`](#insn-00afc5c8)

~~~json
{
  "source": "00afc5c8",
  "target": "00afc608",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc5d8`](#insn-00afc5d8)

~~~json
{
  "source": "00afc5d8",
  "target": "00afc600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc5f0`](#insn-00afc5f0)

~~~json
{
  "source": "00afc5f0",
  "target": "00bddd60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc5fc`](#insn-00afc5fc)

~~~json
{
  "source": "00afc5fc",
  "target": "00afc5dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc60c`](#insn-00afc60c)

~~~json
{
  "source": "00afc60c",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc614`](#insn-00afc614)

~~~json
{
  "source": "00afc614",
  "target": "00bdeca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc61c`](#insn-00afc61c)

~~~json
{
  "source": "00afc61c",
  "target": "00c1b948",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b948",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afc620`](#insn-00afc620)

~~~json
{
  "source": "00afc620",
  "target": "010a0d08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afc628`](#insn-00afc628)

~~~json
{
  "source": "00afc628",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc630`](#insn-00afc630)

~~~json
{
  "source": "00afc630",
  "target": "00c1b940",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b940",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afc634`](#insn-00afc634)

~~~json
{
  "source": "00afc634",
  "target": "010a0d10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afc638`](#insn-00afc638)

~~~json
{
  "source": "00afc638",
  "target": "00afc65c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc640`](#insn-00afc640)

~~~json
{
  "source": "00afc640",
  "target": "00afc65c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc64c`](#insn-00afc64c)

~~~json
{
  "source": "00afc64c",
  "target": "00bdecc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc654`](#insn-00afc654)

~~~json
{
  "source": "00afc654",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc658`](#insn-00afc658)

~~~json
{
  "source": "00afc658",
  "target": "010a0d10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afc660`](#insn-00afc660)

~~~json
{
  "source": "00afc660",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc668`](#insn-00afc668)

~~~json
{
  "source": "00afc668",
  "target": "00afc674",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc670`](#insn-00afc670)

~~~json
{
  "source": "00afc670",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc67c`](#insn-00afc67c)

~~~json
{
  "source": "00afc67c",
  "target": "00bdecb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afc684`](#insn-00afc684)

~~~json
{
  "source": "00afc684",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc688`](#insn-00afc688)

~~~json
{
  "source": "00afc688",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afc690`](#insn-00afc690)

~~~json
{
  "source": "00afc690",
  "target": "00bddc00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
