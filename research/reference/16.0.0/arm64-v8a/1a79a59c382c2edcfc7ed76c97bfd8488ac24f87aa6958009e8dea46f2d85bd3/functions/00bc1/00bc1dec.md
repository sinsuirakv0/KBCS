# 00bc1dec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b53478`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53478.md) · 移動量 `+0x6e974`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0065.md#compare-7584f538f5b59ffa136167c48afc55e5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bc2214`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc2/00bc2214.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0080.md#compare-fc335d230471f6618998ba5e75adfb47)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc1dec",
  "name": "_ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d6a8694e41214d2a7265ccae3f3222f91a9d08c839c0fbebf1e17cf4ba6fa6c9",
  "source_text_sha256": "d6a8694e41214d2a7265ccae3f3222f91a9d08c839c0fbebf1e17cf4ba6fa6c9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc1dec",
        "00bc1e2b"
      ]
    ],
    "bytes_sha256": "e2441f6b1936fec1cf8a832d924a5c1f7fc13e1a0bad6463ca4bac905b7e17c5",
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
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigInfo"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 644 bytes

~~~c

long _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEE
               (void)

{
                    /* try { // try from 00bc1df4 to 00cc1e0f has its CatchHandler @ 00bc1f70 */
  if (DAT_01126168 == 0) {
                    /* try { // try from 00bc1e10 to 00cc1eb7 has its CatchHandler @ 00bc1b44 */
    DAT_01126168 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126168;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc1dec"></a> `00bc1dec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc1df0"></a> `00bc1df0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1df4"></a> `00bc1df4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc1df8"></a> `00bc1df8` | `33 2b 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc1dfc"></a> `00bc1dfc` | `68 b6 40 f9` | ldr x8,[x19, #0x168] | `FALL_THROUGH`
<a id="insn-00bc1e00"></a> `00bc1e00` | `e8 00 00 b5` | cbnz x8,0x00bc1e1c | `CONDITIONAL_JUMP`
<a id="insn-00bc1e04"></a> `00bc1e04` | `23 b7 ff d0` | adrp x3,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bc1e08"></a> `00bc1e08` | `63 30 0c 91` | add x3,x3,#0x30c | `FALL_THROUGH`
<a id="insn-00bc1e0c"></a> `00bc1e0c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bc1e10"></a> `00bc1e10` | `40 63 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bc1e14"></a> `00bc1e14` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bc1e18"></a> `00bc1e18` | `60 b6 00 f9` | str x0,[x19, #0x168] | `FALL_THROUGH`
<a id="insn-00bc1e1c"></a> `00bc1e1c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1e20"></a> `00bc1e20` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bc1e24"></a> `00bc1e24` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc1e28"></a> `00bc1e28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc1dec`](#insn-00bc1dec) 範囲 `[['00bc1dec', '00bc1df3']]`
  - `FALL_THROUGH` [`00bc1df0`](#insn-00bc1df0) → [`00bc1df4`](#insn-00bc1df4)
- ブロック [`00bc1df4`](#insn-00bc1df4) 範囲 `[['00bc1df4', '00bc1e03']]`
  - `CONDITIONAL_JUMP` [`00bc1e00`](#insn-00bc1e00) → [`00bc1e1c`](#insn-00bc1e1c)
  - `FALL_THROUGH` [`00bc1e00`](#insn-00bc1e00) → [`00bc1e04`](#insn-00bc1e04)
- ブロック [`00bc1e04`](#insn-00bc1e04) 範囲 `[['00bc1e04', '00bc1e0f']]`
  - `FALL_THROUGH` [`00bc1e0c`](#insn-00bc1e0c) → [`00bc1e10`](#insn-00bc1e10)
- ブロック [`00bc1e10`](#insn-00bc1e10) 範囲 `[['00bc1e10', '00bc1e1b']]`
  - `FALL_THROUGH` [`00bc1e18`](#insn-00bc1e18) → [`00bc1e1c`](#insn-00bc1e1c)
- ブロック [`00bc1e1c`](#insn-00bc1e1c) 範囲 `[['00bc1e1c', '00bc1e2b']]`

## 命令位置別の参照

- [`00bc1dec`](#insn-00bc1dec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1df0`](#insn-00bc1df0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1dfc`](#insn-00bc1dfc) → `01126168`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc1e00`](#insn-00bc1e00) → [`00bc1e1c`](#insn-00bc1e1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1e08`](#insn-00bc1e08) → `002a730c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc1e10`](#insn-00bc1e10) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bc1e18`](#insn-00bc1e18) → `01126168`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc1e1c`](#insn-00bc1e1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc1dec`](#insn-00bc1dec)

~~~json
{
  "source": "00bc1dec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1df0`](#insn-00bc1df0)

~~~json
{
  "source": "00bc1df0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1dfc`](#insn-00bc1dfc)

~~~json
{
  "source": "00bc1dfc",
  "target": "01126168",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126168",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc1e00`](#insn-00bc1e00)

~~~json
{
  "source": "00bc1e00",
  "target": "00bc1e1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1e08`](#insn-00bc1e08)

~~~json
{
  "source": "00bc1e08",
  "target": "002a730c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7308",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f72656d6f7465636f",
  "capture_start": "002a7308",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc1e10`](#insn-00bc1e10)

~~~json
{
  "source": "00bc1e10",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc1e18`](#insn-00bc1e18)

~~~json
{
  "source": "00bc1e18",
  "target": "01126168",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126168",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc1e1c`](#insn-00bc1e1c)

~~~json
{
  "source": "00bc1e1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
