# 00b5cffc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b5cf60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5cf60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0075.md#compare-9d55ca5c5ac5454ccf7f26f806e9ce9b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b5dff0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5dff0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0008.md#compare-7acfa85e6bafc05b3ebd364c1a4eec0e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5cffc",
  "name": "_ZN8firebase15CleanupNotifier11FindByOwnerEPv",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "93e51db9ef4e727ba91f63c583ba5d3ba0b762329134cf978422309ffb4d54c9",
  "source_text_sha256": "93e51db9ef4e727ba91f63c583ba5d3ba0b762329134cf978422309ffb4d54c9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5cffc",
        "00b5d08b"
      ]
    ],
    "bytes_sha256": "74738893c846ca296cdeaded9b46cb6b790e37219927744d177481799e06bef7",
    "instruction_count": 36,
    "instruction_bytes": 144,
    "body_bytes": 144,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5acc0](../00c5a/00c5acc0.md)

## 呼び出し先

- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3044 bytes

~~~c

long _ZN8firebase15CleanupNotifier11FindByOwnerEPv(ulong param_1)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  undefined8 uVar4;
  long lVar5;
  
                    /* catch() { ... } // from try @ 00b564c8 with catch @ 00b5cffc */
                    /* catch() { ... } // from try @ 00b56468 with catch @ 00b5d000 */
                    /* catch() { ... } // from try @ 00b5645c with catch @ 00b5d004 */
                    /* catch() { ... } // from try @ 00b563ac with catch @ 00b5d008 */
                    /* catch() { ... } // from try @ 00b56304 with catch @ 00b5d00c */
                    /* catch() { ... } // from try @ 00b562f8 with catch @ 00b5d010 */
  uVar4 = *(undefined8 *)
           PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c9b868;
                    /* catch() { ... } // from try @ 00b562e0 with catch @ 00b5d018 */
  _ZN8firebase5Mutex7AcquireEv(uVar4);
                    /* catch() { ... } // from try @ 00b5628c with catch @ 00b5d020 */
                    /* catch() { ... } // from try @ 00b56280 with catch @ 00b5d024 */
                    /* catch() { ... } // from try @ 00b56268 with catch @ 00b5d02c */
  if (*(long *)PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c9b860 != 0) {
    plVar1 = (long *)(*(long *)
                       PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c9b860 + 8)
    ;
    plVar3 = (long *)*plVar1;
                    /* catch() { ... } // from try @ 00b561f4 with catch @ 00b5d034 */
    plVar2 = plVar1;
    if (plVar3 != (long *)0x0) {
      do {
                    /* catch() { ... } // from try @ 00b561cc with catch @ 00b5d040 */
                    /* catch() { ... } // from try @ 00b56178 with catch @ 00b5d048 */
        if ((ulong)plVar3[4] >= param_1) {
          plVar2 = plVar3;
        }
                    /* catch() { ... } // from try @ 00b5616c with catch @ 00b5d04c */
        plVar3 = (long *)plVar3[(ulong)plVar3[4] < param_1];
      } while (plVar3 != (long *)0x0);
                    /* catch() { ... } // from try @ 00b56150 with catch @ 00b5d054 */
                    /* catch() { ... } // from try @ 00b560e8 with catch @ 00b5d05c */
                    /* catch() { ... } // from try @ 00b560dc with catch @ 00b5d060 */
      if ((plVar2 != plVar1) && ((ulong)plVar2[4] <= param_1)) {
                    /* catch() { ... } // from try @ 00b55fdc with catch @ 00b5d084 */
        lVar5 = plVar2[5];
                    /* catch() { ... } // from try @ 00b55fd0 with catch @ 00b5d088 */
        goto LAB_00b5d06c;
      }
    }
  }
                    /* catch() { ... } // from try @ 00b560c0 with catch @ 00b5d068 */
  lVar5 = 0;
LAB_00b5d06c:
                    /* catch() { ... } // from try @ 00b5606c with catch @ 00b5d070 */
  _ZN8firebase5Mutex7ReleaseEv(uVar4);
                    /* catch() { ... } // from try @ 00b56060 with catch @ 00b5d074 */
                    /* catch() { ... } // from try @ 00b56044 with catch @ 00b5d07c */
  return lVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5cffc"></a> `00b5cffc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b5d000"></a> `00b5d000` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5d004"></a> `00b5d004` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b5d008"></a> `00b5d008` | `e8 09 00 d0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00b5d00c"></a> `00b5d00c` | `08 35 44 f9` | ldr x8,[x8, #0x868] | `FALL_THROUGH`
<a id="insn-00b5d010"></a> `00b5d010` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b5d014"></a> `00b5d014` | `13 01 40 f9` | ldr x19,[x8] | `FALL_THROUGH`
<a id="insn-00b5d018"></a> `00b5d018` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5d01c"></a> `00b5d01c` | `ad f6 03 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5d020"></a> `00b5d020` | `e8 09 00 d0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00b5d024"></a> `00b5d024` | `08 31 44 f9` | ldr x8,[x8, #0x860] | `FALL_THROUGH`
<a id="insn-00b5d028"></a> `00b5d028` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00b5d02c"></a> `00b5d02c` | `e8 01 00 b4` | cbz x8,0x00b5d068 | `CONDITIONAL_JUMP`
<a id="insn-00b5d030"></a> `00b5d030` | `0a 8d 40 f8` | ldr x10,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00b5d034"></a> `00b5d034` | `aa 01 00 b4` | cbz x10,0x00b5d068 | `CONDITIONAL_JUMP`
<a id="insn-00b5d038"></a> `00b5d038` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00b5d03c"></a> `00b5d03c` | `4b 11 40 f9` | ldr x11,[x10, #0x20] | `FALL_THROUGH`
<a id="insn-00b5d040"></a> `00b5d040` | `7f 01 14 eb` | cmp x11,x20 | `FALL_THROUGH`
<a id="insn-00b5d044"></a> `00b5d044` | `eb 27 9f 1a` | cset w11,cc | `FALL_THROUGH`
<a id="insn-00b5d048"></a> `00b5d048` | `29 31 8a 9a` | csel x9,x9,x10,cc | `FALL_THROUGH`
<a id="insn-00b5d04c"></a> `00b5d04c` | `4a 59 6b f8` | ldr x10,[x10, w11, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00b5d050"></a> `00b5d050` | `6a ff ff b5` | cbnz x10,0x00b5d03c | `CONDITIONAL_JUMP`
<a id="insn-00b5d054"></a> `00b5d054` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00b5d058"></a> `00b5d058` | `80 00 00 54` | b.eq 0x00b5d068 | `CONDITIONAL_JUMP`
<a id="insn-00b5d05c"></a> `00b5d05c` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00b5d060"></a> `00b5d060` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00b5d064"></a> `00b5d064` | `09 01 00 54` | b.ls 0x00b5d084 | `CONDITIONAL_JUMP`
<a id="insn-00b5d068"></a> `00b5d068` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00b5d06c"></a> `00b5d06c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5d070"></a> `00b5d070` | `9c f6 03 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5d074"></a> `00b5d074` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5d078"></a> `00b5d078` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b5d07c"></a> `00b5d07c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b5d080"></a> `00b5d080` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5d084"></a> `00b5d084` | `34 15 40 f9` | ldr x20,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00b5d088"></a> `00b5d088` | `f9 ff ff 17` | b 0x00b5d06c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b5cffc`](#insn-00b5cffc) 範囲 `[['00b5cffc', '00b5cfff']]`
  - `FALL_THROUGH` [`00b5cffc`](#insn-00b5cffc) → [`00b5d000`](#insn-00b5d000)
- ブロック [`00b5d000`](#insn-00b5d000) 範囲 `[['00b5d000', '00b5d003']]`
  - `FALL_THROUGH` [`00b5d000`](#insn-00b5d000) → [`00b5d004`](#insn-00b5d004)
- ブロック [`00b5d004`](#insn-00b5d004) 範囲 `[['00b5d004', '00b5d007']]`
  - `FALL_THROUGH` [`00b5d004`](#insn-00b5d004) → [`00b5d008`](#insn-00b5d008)
- ブロック [`00b5d008`](#insn-00b5d008) 範囲 `[['00b5d008', '00b5d00b']]`
  - `FALL_THROUGH` [`00b5d008`](#insn-00b5d008) → [`00b5d00c`](#insn-00b5d00c)
- ブロック [`00b5d00c`](#insn-00b5d00c) 範囲 `[['00b5d00c', '00b5d00f']]`
  - `FALL_THROUGH` [`00b5d00c`](#insn-00b5d00c) → [`00b5d010`](#insn-00b5d010)
- ブロック [`00b5d010`](#insn-00b5d010) 範囲 `[['00b5d010', '00b5d017']]`
  - `FALL_THROUGH` [`00b5d014`](#insn-00b5d014) → [`00b5d018`](#insn-00b5d018)
- ブロック [`00b5d018`](#insn-00b5d018) 範囲 `[['00b5d018', '00b5d01f']]`
  - `FALL_THROUGH` [`00b5d01c`](#insn-00b5d01c) → [`00b5d020`](#insn-00b5d020)
- ブロック [`00b5d020`](#insn-00b5d020) 範囲 `[['00b5d020', '00b5d023']]`
  - `FALL_THROUGH` [`00b5d020`](#insn-00b5d020) → [`00b5d024`](#insn-00b5d024)
- ブロック [`00b5d024`](#insn-00b5d024) 範囲 `[['00b5d024', '00b5d02b']]`
  - `FALL_THROUGH` [`00b5d028`](#insn-00b5d028) → [`00b5d02c`](#insn-00b5d02c)
- ブロック [`00b5d02c`](#insn-00b5d02c) 範囲 `[['00b5d02c', '00b5d02f']]`
  - `CONDITIONAL_JUMP` [`00b5d02c`](#insn-00b5d02c) → [`00b5d068`](#insn-00b5d068)
  - `FALL_THROUGH` [`00b5d02c`](#insn-00b5d02c) → [`00b5d030`](#insn-00b5d030)
- ブロック [`00b5d030`](#insn-00b5d030) 範囲 `[['00b5d030', '00b5d033']]`
  - `FALL_THROUGH` [`00b5d030`](#insn-00b5d030) → [`00b5d034`](#insn-00b5d034)
- ブロック [`00b5d034`](#insn-00b5d034) 範囲 `[['00b5d034', '00b5d037']]`
  - `CONDITIONAL_JUMP` [`00b5d034`](#insn-00b5d034) → [`00b5d068`](#insn-00b5d068)
  - `FALL_THROUGH` [`00b5d034`](#insn-00b5d034) → [`00b5d038`](#insn-00b5d038)
- ブロック [`00b5d038`](#insn-00b5d038) 範囲 `[['00b5d038', '00b5d03b']]`
  - `FALL_THROUGH` [`00b5d038`](#insn-00b5d038) → [`00b5d03c`](#insn-00b5d03c)
- ブロック [`00b5d03c`](#insn-00b5d03c) 範囲 `[['00b5d03c', '00b5d03f']]`
  - `FALL_THROUGH` [`00b5d03c`](#insn-00b5d03c) → [`00b5d040`](#insn-00b5d040)
- ブロック [`00b5d040`](#insn-00b5d040) 範囲 `[['00b5d040', '00b5d047']]`
  - `FALL_THROUGH` [`00b5d044`](#insn-00b5d044) → [`00b5d048`](#insn-00b5d048)
- ブロック [`00b5d048`](#insn-00b5d048) 範囲 `[['00b5d048', '00b5d04b']]`
  - `FALL_THROUGH` [`00b5d048`](#insn-00b5d048) → [`00b5d04c`](#insn-00b5d04c)
- ブロック [`00b5d04c`](#insn-00b5d04c) 範囲 `[['00b5d04c', '00b5d053']]`
  - `CONDITIONAL_JUMP` [`00b5d050`](#insn-00b5d050) → [`00b5d03c`](#insn-00b5d03c)
  - `FALL_THROUGH` [`00b5d050`](#insn-00b5d050) → [`00b5d054`](#insn-00b5d054)
- ブロック [`00b5d054`](#insn-00b5d054) 範囲 `[['00b5d054', '00b5d05b']]`
  - `CONDITIONAL_JUMP` [`00b5d058`](#insn-00b5d058) → [`00b5d068`](#insn-00b5d068)
  - `FALL_THROUGH` [`00b5d058`](#insn-00b5d058) → [`00b5d05c`](#insn-00b5d05c)
- ブロック [`00b5d05c`](#insn-00b5d05c) 範囲 `[['00b5d05c', '00b5d05f']]`
  - `FALL_THROUGH` [`00b5d05c`](#insn-00b5d05c) → [`00b5d060`](#insn-00b5d060)
- ブロック [`00b5d060`](#insn-00b5d060) 範囲 `[['00b5d060', '00b5d067']]`
  - `CONDITIONAL_JUMP` [`00b5d064`](#insn-00b5d064) → [`00b5d084`](#insn-00b5d084)
  - `FALL_THROUGH` [`00b5d064`](#insn-00b5d064) → [`00b5d068`](#insn-00b5d068)
- ブロック [`00b5d068`](#insn-00b5d068) 範囲 `[['00b5d068', '00b5d06b']]`
  - `FALL_THROUGH` [`00b5d068`](#insn-00b5d068) → [`00b5d06c`](#insn-00b5d06c)
- ブロック [`00b5d06c`](#insn-00b5d06c) 範囲 `[['00b5d06c', '00b5d06f']]`
  - `FALL_THROUGH` [`00b5d06c`](#insn-00b5d06c) → [`00b5d070`](#insn-00b5d070)
- ブロック [`00b5d070`](#insn-00b5d070) 範囲 `[['00b5d070', '00b5d073']]`
  - `FALL_THROUGH` [`00b5d070`](#insn-00b5d070) → [`00b5d074`](#insn-00b5d074)
- ブロック [`00b5d074`](#insn-00b5d074) 範囲 `[['00b5d074', '00b5d07b']]`
  - `FALL_THROUGH` [`00b5d078`](#insn-00b5d078) → [`00b5d07c`](#insn-00b5d07c)
- ブロック [`00b5d07c`](#insn-00b5d07c) 範囲 `[['00b5d07c', '00b5d083']]`
- ブロック [`00b5d084`](#insn-00b5d084) 範囲 `[['00b5d084', '00b5d087']]`
  - `FALL_THROUGH` [`00b5d084`](#insn-00b5d084) → [`00b5d088`](#insn-00b5d088)
- ブロック [`00b5d088`](#insn-00b5d088) 範囲 `[['00b5d088', '00b5d08b']]`
  - `UNCONDITIONAL_JUMP` [`00b5d088`](#insn-00b5d088) → [`00b5d06c`](#insn-00b5d06c)

## 命令位置別の参照

- [`00b5cffc`](#insn-00b5cffc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5d000`](#insn-00b5d000) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5d00c`](#insn-00b5d00c) → `00c9b868`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b5d014`](#insn-00b5d014) → `01126108`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E` · 推定型 `undefined8`
- [`00b5d01c`](#insn-00b5d01c) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00b5d024`](#insn-00b5d024) → `00c9b860`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b5d028`](#insn-00b5d028) → `01126110`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E` · 推定型 `undefined8`
- [`00b5d02c`](#insn-00b5d02c) → [`00b5d068`](#insn-00b5d068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5d034`](#insn-00b5d034) → [`00b5d068`](#insn-00b5d068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5d050`](#insn-00b5d050) → [`00b5d03c`](#insn-00b5d03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5d058`](#insn-00b5d058) → [`00b5d068`](#insn-00b5d068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5d064`](#insn-00b5d064) → [`00b5d084`](#insn-00b5d084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5d070`](#insn-00b5d070) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00b5d074`](#insn-00b5d074) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5d088`](#insn-00b5d088) → [`00b5d06c`](#insn-00b5d06c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5cffc`](#insn-00b5cffc)

~~~json
{
  "source": "00b5cffc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5d000`](#insn-00b5d000)

~~~json
{
  "source": "00b5d000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5d00c`](#insn-00b5d00c)

~~~json
{
  "source": "00b5d00c",
  "target": "00c9b868",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b868",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b5d014`](#insn-00b5d014)

~~~json
{
  "source": "00b5d014",
  "target": "01126108",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126108",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5d01c`](#insn-00b5d01c)

~~~json
{
  "source": "00b5d01c",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5d024`](#insn-00b5d024)

~~~json
{
  "source": "00b5d024",
  "target": "00c9b860",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b860",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b5d028`](#insn-00b5d028)

~~~json
{
  "source": "00b5d028",
  "target": "01126110",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126110",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5d02c`](#insn-00b5d02c)

~~~json
{
  "source": "00b5d02c",
  "target": "00b5d068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5d034`](#insn-00b5d034)

~~~json
{
  "source": "00b5d034",
  "target": "00b5d068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5d050`](#insn-00b5d050)

~~~json
{
  "source": "00b5d050",
  "target": "00b5d03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5d058`](#insn-00b5d058)

~~~json
{
  "source": "00b5d058",
  "target": "00b5d068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5d064`](#insn-00b5d064)

~~~json
{
  "source": "00b5d064",
  "target": "00b5d084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5d070`](#insn-00b5d070)

~~~json
{
  "source": "00b5d070",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5d074`](#insn-00b5d074)

~~~json
{
  "source": "00b5d074",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5d088`](#insn-00b5d088)

~~~json
{
  "source": "00b5d088",
  "target": "00b5d06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
