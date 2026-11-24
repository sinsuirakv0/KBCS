# 00b5bfcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afc248`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc248.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0060.md#compare-fbb7df1617faa1973672c68165e0361d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b5c3f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c3f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0008.md#compare-e8e364195f2ba4f056e99b014a73f08f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5bfcc",
  "name": "_ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED2Ev",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "47f0da81cf6ffaf94a21baeab889d4505a46bf40f309bd6e2903c330aad1bce5",
  "source_text_sha256": "47f0da81cf6ffaf94a21baeab889d4505a46bf40f309bd6e2903c330aad1bce5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5bfcc",
        "00b5c047"
      ]
    ],
    "bytes_sha256": "57c4ef108215f800eec2ae785d5fb7953ffa98d8d8081261e8bbcecd7c12366a",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57aa0](../00c57/00c57aa0.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 718 bytes

~~~c

void _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED2Ev
               (long *param_1)

{
  long lVar1;
  long *plVar2;
  
  lVar1 = param_1[4];
  *param_1 = (long)(
                   PTR__ZTVNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEEE_00c9b388
                   + 0x10);
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  if (((char)param_1[5] == '\0') && (plVar2 = (long *)param_1[3], plVar2 != (long *)0x0)) {
    param_1[3] = 0;
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
    (**(code **)(*plVar2 + 8))(plVar2);
  }
  else {
    _ZN8firebase5Mutex7ReleaseEv(lVar1);
  }
  _ZNSt6__ndk119__shared_weak_countD1Ev(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5bfcc"></a> `00b5bfcc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b5bfd0"></a> `00b5bfd0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bfd4"></a> `00b5bfd4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5bfd8"></a> `00b5bfd8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b5bfdc"></a> `00b5bfdc` | `08 0a 00 90` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00b5bfe0"></a> `00b5bfe0` | `14 10 40 f9` | ldr x20,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00b5bfe4"></a> `00b5bfe4` | `08 c5 41 f9` | ldr x8,[x8, #0x388] | `FALL_THROUGH`
<a id="insn-00b5bfe8"></a> `00b5bfe8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b5bfec"></a> `00b5bfec` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b5bff0"></a> `00b5bff0` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00b5bff4"></a> `00b5bff4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b5bff8"></a> `00b5bff8` | `82 f9 03 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bffc"></a> `00b5bffc` | `68 a2 40 39` | ldrb w8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b5c000"></a> `00b5c000` | `88 00 00 34` | cbz w8,0x00b5c010 | `CONDITIONAL_JUMP`
<a id="insn-00b5c004"></a> `00b5c004` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b5c008"></a> `00b5c008` | `82 f9 03 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00b5c00c"></a> `00b5c00c` | `0a 00 00 14` | b 0x00b5c034 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5c010"></a> `00b5c010` | `75 0e 40 f9` | ldr x21,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b5c014"></a> `00b5c014` | `95 ff ff b4` | cbz x21,0x00b5c004 | `CONDITIONAL_JUMP`
<a id="insn-00b5c018"></a> `00b5c018` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b5c01c"></a> `00b5c01c` | `7f 0e 00 f9` | str xzr,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b5c020"></a> `00b5c020` | `7c f9 03 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00b5c024"></a> `00b5c024` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00b5c028"></a> `00b5c028` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b5c02c"></a> `00b5c02c` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b5c030"></a> `00b5c030` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5c034"></a> `00b5c034` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5c038"></a> `00b5c038` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5c03c"></a> `00b5c03c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5c040"></a> `00b5c040` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b5c044"></a> `00b5c044` | `97 ee 03 14` | b 0x00c57aa0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5bfcc`](#insn-00b5bfcc) 範囲 `[['00b5bfcc', '00b5c003']]`
  - `CONDITIONAL_JUMP` [`00b5c000`](#insn-00b5c000) → [`00b5c010`](#insn-00b5c010)
  - `FALL_THROUGH` [`00b5c000`](#insn-00b5c000) → [`00b5c004`](#insn-00b5c004)
- ブロック [`00b5c004`](#insn-00b5c004) 範囲 `[['00b5c004', '00b5c00f']]`
  - `UNCONDITIONAL_JUMP` [`00b5c00c`](#insn-00b5c00c) → [`00b5c034`](#insn-00b5c034)
- ブロック [`00b5c010`](#insn-00b5c010) 範囲 `[['00b5c010', '00b5c017']]`
  - `CONDITIONAL_JUMP` [`00b5c014`](#insn-00b5c014) → [`00b5c004`](#insn-00b5c004)
  - `FALL_THROUGH` [`00b5c014`](#insn-00b5c014) → [`00b5c018`](#insn-00b5c018)
- ブロック [`00b5c018`](#insn-00b5c018) 範囲 `[['00b5c018', '00b5c033']]`
  - `FALL_THROUGH` [`00b5c030`](#insn-00b5c030) → [`00b5c034`](#insn-00b5c034)
- ブロック [`00b5c034`](#insn-00b5c034) 範囲 `[['00b5c034', '00b5c047']]`

## 命令位置別の参照

- [`00b5bfcc`](#insn-00b5bfcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bfd0`](#insn-00b5bfd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bfd4`](#insn-00b5bfd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bfe4`](#insn-00b5bfe4) → `00c9b388`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b5bff0`](#insn-00b5bff0) → `00c8ff18`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[56]`
- [`00b5bff8`](#insn-00b5bff8) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00b5c000`](#insn-00b5c000) → [`00b5c010`](#insn-00b5c010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5c008`](#insn-00b5c008) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00b5c00c`](#insn-00b5c00c) → [`00b5c034`](#insn-00b5c034) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5c014`](#insn-00b5c014) → [`00b5c004`](#insn-00b5c004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5c020`](#insn-00b5c020) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00b5c038`](#insn-00b5c038) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5c03c`](#insn-00b5c03c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5c044`](#insn-00b5c044) → [`00c57aa0`](../00c57/00c57aa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57aa0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5bfcc`](#insn-00b5bfcc)

~~~json
{
  "source": "00b5bfcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bfd0`](#insn-00b5bfd0)

~~~json
{
  "source": "00b5bfd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bfd4`](#insn-00b5bfd4)

~~~json
{
  "source": "00b5bfd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bfe4`](#insn-00b5bfe4)

~~~json
{
  "source": "00b5bfe4",
  "target": "00c9b388",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b388",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b5bff0`](#insn-00b5bff0)

~~~json
{
  "source": "00b5bff0",
  "target": "00c8ff18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8ff08",
  "offset": 16,
  "size": 56,
  "datatype": "undefined1[56]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00b5bff8`](#insn-00b5bff8)

~~~json
{
  "source": "00b5bff8",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5c000`](#insn-00b5c000)

~~~json
{
  "source": "00b5c000",
  "target": "00b5c010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5c008`](#insn-00b5c008)

~~~json
{
  "source": "00b5c008",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5c00c`](#insn-00b5c00c)

~~~json
{
  "source": "00b5c00c",
  "target": "00b5c034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5c014`](#insn-00b5c014)

~~~json
{
  "source": "00b5c014",
  "target": "00b5c004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5c020`](#insn-00b5c020)

~~~json
{
  "source": "00b5c020",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5c038`](#insn-00b5c038)

~~~json
{
  "source": "00b5c038",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5c03c`](#insn-00b5c03c)

~~~json
{
  "source": "00b5c03c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5c044`](#insn-00b5c044)

~~~json
{
  "source": "00b5c044",
  "target": "00c57aa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
