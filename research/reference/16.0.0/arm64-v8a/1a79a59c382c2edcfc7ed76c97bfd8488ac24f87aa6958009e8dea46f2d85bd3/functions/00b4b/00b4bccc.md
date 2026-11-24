# 00b4bccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aebf48`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf48.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-5ba74b1c76a58cb131f89f999dd0803a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b4c0f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4c/00b4c0f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0072.md#compare-803a9bc8f75edbc6b4bfebf97b57cc19)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4bccc",
  "name": "_ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "335816890ea3109ae9a1dbe45f5a760aab4c34ecae601ba284f57ca200a0f6ba",
  "source_text_sha256": "335816890ea3109ae9a1dbe45f5a760aab4c34ecae601ba284f57ca200a0f6ba",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4bccc",
        "00b4bd0b"
      ]
    ],
    "bytes_sha256": "6a94139e10d56e1d6de515b9ec2c36c5451137c1a3add65bb9dc08e91140c99c",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"java/util/List"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 423 bytes

~~~c

long _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE
               (void)

{
  if (DAT_011257e0 == 0) {
    DAT_011257e0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_011257e0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4bccc"></a> `00b4bccc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4bcd0"></a> `00b4bcd0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4bcd4"></a> `00b4bcd4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4bcd8"></a> `00b4bcd8` | `d3 2e 00 d0` | adrp x19,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4bcdc"></a> `00b4bcdc` | `68 f2 43 f9` | ldr x8,[x19, #0x7e0] | `FALL_THROUGH`
<a id="insn-00b4bce0"></a> `00b4bce0` | `e8 00 00 b5` | cbnz x8,0x00b4bcfc | `CONDITIONAL_JUMP`
<a id="insn-00b4bce4"></a> `00b4bce4` | `a3 ba ff 90` | adrp x3,0x29f000 | `FALL_THROUGH`
<a id="insn-00b4bce8"></a> `00b4bce8` | `63 f0 22 91` | add x3,x3,#0x8bc | `FALL_THROUGH`
<a id="insn-00b4bcec"></a> `00b4bcec` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b4bcf0"></a> `00b4bcf0` | `88 3b 04 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00b4bcf4"></a> `00b4bcf4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4bcf8"></a> `00b4bcf8` | `60 f2 03 f9` | str x0,[x19, #0x7e0] | `FALL_THROUGH`
<a id="insn-00b4bcfc"></a> `00b4bcfc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4bd00"></a> `00b4bd00` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4bd04"></a> `00b4bd04` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4bd08"></a> `00b4bd08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4bccc`](#insn-00b4bccc) 範囲 `[['00b4bccc', '00b4bce3']]`
  - `CONDITIONAL_JUMP` [`00b4bce0`](#insn-00b4bce0) → [`00b4bcfc`](#insn-00b4bcfc)
  - `FALL_THROUGH` [`00b4bce0`](#insn-00b4bce0) → [`00b4bce4`](#insn-00b4bce4)
- ブロック [`00b4bce4`](#insn-00b4bce4) 範囲 `[['00b4bce4', '00b4bcfb']]`
  - `FALL_THROUGH` [`00b4bcf8`](#insn-00b4bcf8) → [`00b4bcfc`](#insn-00b4bcfc)
- ブロック [`00b4bcfc`](#insn-00b4bcfc) 範囲 `[['00b4bcfc', '00b4bd0b']]`

## 命令位置別の参照

- [`00b4bccc`](#insn-00b4bccc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bcd0`](#insn-00b4bcd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bcdc`](#insn-00b4bcdc) → `011257e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4bce0`](#insn-00b4bce0) → [`00b4bcfc`](#insn-00b4bcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4bce8`](#insn-00b4bce8) → `0029f8bc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4bcf0`](#insn-00b4bcf0) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00b4bcf8`](#insn-00b4bcf8) → `011257e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4bcfc`](#insn-00b4bcfc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4bccc`](#insn-00b4bccc)

~~~json
{
  "source": "00b4bccc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bcd0`](#insn-00b4bcd0)

~~~json
{
  "source": "00b4bcd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bcdc`](#insn-00b4bcdc)

~~~json
{
  "source": "00b4bcdc",
  "target": "011257e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011257e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bce0`](#insn-00b4bce0)

~~~json
{
  "source": "00b4bce0",
  "target": "00b4bcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4bce8`](#insn-00b4bce8)

~~~json
{
  "source": "00b4bce8",
  "target": "0029f8bc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029f8bc",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4c69737400",
  "capture_start": "0029f8bc",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4bcf0`](#insn-00b4bcf0)

~~~json
{
  "source": "00b4bcf0",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4bcf8`](#insn-00b4bcf8)

~~~json
{
  "source": "00b4bcf8",
  "target": "011257e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011257e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4bcfc`](#insn-00b4bcfc)

~~~json
{
  "source": "00b4bcfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
