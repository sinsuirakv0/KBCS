# 00b4adec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeb068`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb068.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-535e77f32ffb00fdfa3c636f731a58b7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b4b214`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b4b/00b4b214.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0072.md#compare-cb97fa384438372c708f4bf7b018959d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4adec",
  "name": "_ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3374900278ebb3c10ffa9b8ec61d21fe342935eec45b798ab83c5b3c04bacb94",
  "source_text_sha256": "3374900278ebb3c10ffa9b8ec61d21fe342935eec45b798ab83c5b3c04bacb94",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b4adec",
        "00b4ae2b"
      ]
    ],
    "bytes_sha256": "8678364294860dc56c56fd87ee9d7a7d3cd177e1e50d328b89afaa1464c7149f",
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
"java/lang/Integer"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 456 bytes

~~~c

long _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16ClassRequirementE
               (void)

{
  if (DAT_01125730 == 0) {
    DAT_01125730 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01125730;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b4adec"></a> `00b4adec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b4adf0"></a> `00b4adf0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4adf4"></a> `00b4adf4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b4adf8"></a> `00b4adf8` | `d3 2e 00 f0` | adrp x19,0x1125000 | `FALL_THROUGH`
<a id="insn-00b4adfc"></a> `00b4adfc` | `68 9a 43 f9` | ldr x8,[x19, #0x730] | `FALL_THROUGH`
<a id="insn-00b4ae00"></a> `00b4ae00` | `e8 00 00 b5` | cbnz x8,0x00b4ae1c | `CONDITIONAL_JUMP`
<a id="insn-00b4ae04"></a> `00b4ae04` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00b4ae08"></a> `00b4ae08` | `e3 ba ff d0` | adrp x3,0x2a8000 | `FALL_THROUGH`
<a id="insn-00b4ae0c"></a> `00b4ae0c` | `63 94 0d 91` | add x3,x3,#0x365 | `FALL_THROUGH`
<a id="insn-00b4ae10"></a> `00b4ae10` | `40 3f 04 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00b4ae14"></a> `00b4ae14` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b4ae18"></a> `00b4ae18` | `60 9a 03 f9` | str x0,[x19, #0x730] | `FALL_THROUGH`
<a id="insn-00b4ae1c"></a> `00b4ae1c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b4ae20"></a> `00b4ae20` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b4ae24"></a> `00b4ae24` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b4ae28"></a> `00b4ae28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b4adec`](#insn-00b4adec) 範囲 `[['00b4adec', '00b4ae03']]`
  - `CONDITIONAL_JUMP` [`00b4ae00`](#insn-00b4ae00) → [`00b4ae1c`](#insn-00b4ae1c)
  - `FALL_THROUGH` [`00b4ae00`](#insn-00b4ae00) → [`00b4ae04`](#insn-00b4ae04)
- ブロック [`00b4ae04`](#insn-00b4ae04) 範囲 `[['00b4ae04', '00b4ae1b']]`
  - `FALL_THROUGH` [`00b4ae18`](#insn-00b4ae18) → [`00b4ae1c`](#insn-00b4ae1c)
- ブロック [`00b4ae1c`](#insn-00b4ae1c) 範囲 `[['00b4ae1c', '00b4ae2b']]`

## 命令位置別の参照

- [`00b4adec`](#insn-00b4adec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4adf0`](#insn-00b4adf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4adfc`](#insn-00b4adfc) → `01125730`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ae00`](#insn-00b4ae00) → [`00b4ae1c`](#insn-00b4ae1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b4ae0c`](#insn-00b4ae0c) → `002a8365`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b4ae10`](#insn-00b4ae10) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00b4ae18`](#insn-00b4ae18) → `01125730`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b4ae1c`](#insn-00b4ae1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b4adec`](#insn-00b4adec)

~~~json
{
  "source": "00b4adec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4adf0`](#insn-00b4adf0)

~~~json
{
  "source": "00b4adf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4adfc`](#insn-00b4adfc)

~~~json
{
  "source": "00b4adfc",
  "target": "01125730",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125730",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ae00`](#insn-00b4ae00)

~~~json
{
  "source": "00b4ae00",
  "target": "00b4ae1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b4ae0c`](#insn-00b4ae0c)

~~~json
{
  "source": "00b4ae0c",
  "target": "002a8365",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8365",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f496e746567657200",
  "capture_start": "002a8365",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00b4ae10`](#insn-00b4ae10)

~~~json
{
  "source": "00b4ae10",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b4ae18`](#insn-00b4ae18)

~~~json
{
  "source": "00b4ae18",
  "target": "01125730",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125730",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b4ae1c`](#insn-00b4ae1c)

~~~json
{
  "source": "00b4ae1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
