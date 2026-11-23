# 006fecac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `006fecac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006fe/006fecac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0009.md#compare-7e419febc9f53de4a4ede59e162a35b5)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `006fecac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006fe/006fecac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/no_difference_in_scope-0008.md#compare-09f6941e09e3a6b0489a3193d18148c7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fecac",
  "name": "FUN_006fecac",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1ea20d6be60f4f58a1c1be017f44d107fa6444c35ed7a1ff06f20ed0f05cc274",
  "source_text_sha256": "1ea20d6be60f4f58a1c1be017f44d107fa6444c35ed7a1ff06f20ed0f05cc274",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006fecac",
        "006fed07"
      ]
    ],
    "bytes_sha256": "2604c8654b43985dc28ee20a1051d40a5999d7e14622f8a9f3140906c9462abe",
    "instruction_count": 23,
    "instruction_bytes": 92,
    "body_bytes": 92,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00734830](../00734/00734830.md)
- [0073496c](../00734/0073496c.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1114 bytes

~~~c

undefined4 FUN_006fecac(uint param_1)

{
  uint uVar1;
  long lVar2;
  long lVar3;
  
                    /* catch() { ... } // from try @ 006fe914 with catch @ 006fecac */
                    /* catch() { ... } // from try @ 006fe688 with catch @ 006fecb0 */
                    /* catch() { ... } // from try @ 006fea64 with catch @ 006fecb4
                       catch() { ... } // from try @ 006fec4c with catch @ 006fecb4 */
                    /* catch() { ... } // from try @ 006fea90 with catch @ 006fecbc */
  lVar2 = FUN_0081f580();
  lVar3 = FUN_0081f580();
                    /* catch() { ... } // from try @ 006fe9bc with catch @ 006feccc
                       catch() { ... } // from try @ 006fec34 with catch @ 006feccc */
                    /* catch() { ... } // from try @ 006fea04 with catch @ 006fecd4 */
  uVar1 = *(int *)(BYTE_ARRAY_00343241 + lVar3 + 0x23) + ~param_1 &
          ((int)(*(int *)(BYTE_ARRAY_00343241 + lVar3 + 0x23) + ~param_1) >> 0x1f ^ 0xffffffffU);
  if (0x1f2 < uVar1) {
    uVar1 = 499;
  }
  return *(undefined4 *)(&uleb128_00389fd0 + lVar2 + (ulong)uVar1 * 4);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006fecac"></a> `006fecac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-006fecb0"></a> `006fecb0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fecb4"></a> `006fecb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006fecb8"></a> `006fecb8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-006fecbc"></a> `006fecbc` | `31 82 04 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-006fecc0"></a> `006fecc0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-006fecc4"></a> `006fecc4` | `2f 82 04 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-006fecc8"></a> `006fecc8` | `88 4c 86 52` | mov w8,#0x3264 | `FALL_THROUGH`
<a id="insn-006feccc"></a> `006feccc` | `e9 03 33 2a` | mvn w9,w19 | `FALL_THROUGH`
<a id="insn-006fecd0"></a> `006fecd0` | `88 06 a0 72` | movk w8,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-006fecd4"></a> `006fecd4` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006fecd8"></a> `006fecd8` | `08 01 09 0b` | add w8,w8,w9 | `FALL_THROUGH`
<a id="insn-006fecdc"></a> `006fecdc` | `69 3e 80 52` | mov w9,#0x1f3 | `FALL_THROUGH`
<a id="insn-006fece0"></a> `006fece0` | `08 7d a8 0a` | bic w8,w8,w8, ASR #0x1f | `FALL_THROUGH`
<a id="insn-006fece4"></a> `006fece4` | `1f cd 07 71` | cmp w8,#0x1f3 | `FALL_THROUGH`
<a id="insn-006fece8"></a> `006fece8` | `08 31 89 1a` | csel w8,w8,w9,cc | `FALL_THROUGH`
<a id="insn-006fecec"></a> `006fecec` | `09 fa 93 52` | mov w9,#0x9fd0 | `FALL_THROUGH`
<a id="insn-006fecf0"></a> `006fecf0` | `88 4a 28 8b` | add x8,x20,w8, UXTW  #0x2 | `FALL_THROUGH`
<a id="insn-006fecf4"></a> `006fecf4` | `09 07 a0 72` | movk w9,#0x38, LSL #16 | `FALL_THROUGH`
<a id="insn-006fecf8"></a> `006fecf8` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006fecfc"></a> `006fecfc` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fed00"></a> `006fed00` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-006fed04"></a> `006fed04` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006fecac`](#insn-006fecac) 範囲 `[['006fecac', '006fecaf']]`
  - `FALL_THROUGH` [`006fecac`](#insn-006fecac) → [`006fecb0`](#insn-006fecb0)
- ブロック [`006fecb0`](#insn-006fecb0) 範囲 `[['006fecb0', '006fecb3']]`
  - `FALL_THROUGH` [`006fecb0`](#insn-006fecb0) → [`006fecb4`](#insn-006fecb4)
- ブロック [`006fecb4`](#insn-006fecb4) 範囲 `[['006fecb4', '006fecbb']]`
  - `FALL_THROUGH` [`006fecb8`](#insn-006fecb8) → [`006fecbc`](#insn-006fecbc)
- ブロック [`006fecbc`](#insn-006fecbc) 範囲 `[['006fecbc', '006feccb']]`
  - `FALL_THROUGH` [`006fecc8`](#insn-006fecc8) → [`006feccc`](#insn-006feccc)
- ブロック [`006feccc`](#insn-006feccc) 範囲 `[['006feccc', '006fecd3']]`
  - `FALL_THROUGH` [`006fecd0`](#insn-006fecd0) → [`006fecd4`](#insn-006fecd4)
- ブロック [`006fecd4`](#insn-006fecd4) 範囲 `[['006fecd4', '006fed07']]`

## 命令位置別の参照

- [`006fecac`](#insn-006fecac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fecb0`](#insn-006fecb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fecbc`](#insn-006fecbc) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`006fecc4`](#insn-006fecc4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`006fecd4`](#insn-006fecd4) → `00343264`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[55]`
- [`006fecf8`](#insn-006fecf8) → `0038a79c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[51]`
- [`006fecf8`](#insn-006fecf8) → `00389fd0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`006fecfc`](#insn-006fecfc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fed00`](#insn-006fed00) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006fecac`](#insn-006fecac)

~~~json
{
  "source": "006fecac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fecb0`](#insn-006fecb0)

~~~json
{
  "source": "006fecb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fecbc`](#insn-006fecbc)

~~~json
{
  "source": "006fecbc",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fecc4`](#insn-006fecc4)

~~~json
{
  "source": "006fecc4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fecd4`](#insn-006fecd4)

~~~json
{
  "source": "006fecd4",
  "target": "00343264",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00343241",
  "offset": 35,
  "size": 55,
  "datatype": "byte[55]",
  "bytes": "440e40500c1d409302940495069608970c9e0e9d100a035c030c1f40500e00d3",
  "capture_start": "00343241",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006fecf8`](#insn-006fecf8)

~~~json
{
  "source": "006fecf8",
  "target": "0038a79c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038a791",
  "offset": 11,
  "size": 51,
  "datatype": "byte[51]",
  "bytes": "440e20480c1d2093049e069d080a700c1f20480e00d3dedd440b0a480c1f2048",
  "capture_start": "0038a791",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006fecf8`](#insn-006fecf8)

~~~json
{
  "source": "006fecf8",
  "target": "00389fd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00389fd0",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "00389fd0",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006fecfc`](#insn-006fecfc)

~~~json
{
  "source": "006fecfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fed00`](#insn-006fed00)

~~~json
{
  "source": "006fed00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
