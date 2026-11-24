# 00bcc8bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5d3bc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d3bc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-466aa54fd6bf3e068fd21efd849de657)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bccce4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bccce4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-c221feea69953019f3d4b21a8099eefb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcc8bc",
  "name": "_ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "148b24e7cc244f5f8fea9348bb4fe3d9629ee27891a8cdff44b82a2df663e189",
  "source_text_sha256": "148b24e7cc244f5f8fea9348bb4fe3d9629ee27891a8cdff44b82a2df663e189",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcc8bc",
        "00bcc8fb"
      ]
    ],
    "bytes_sha256": "38d2a2de34a3c511019a1692b1da614a8d029602862ee204a11e803c21598805",
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
"com/google/firebase/auth/internal/cpp/JniIdTokenListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 565 bytes

~~~c

long _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
  if (DAT_01126418 == 0) {
    DAT_01126418 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
                    /* try { // try from 00bcc8f4 to 00ccc90b has its CatchHandler @ 00bce70c */
  return DAT_01126418;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcc8bc"></a> `00bcc8bc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcc8c0"></a> `00bcc8c0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc8c4"></a> `00bcc8c4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcc8c8"></a> `00bcc8c8` | `d3 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcc8cc"></a> `00bcc8cc` | `68 0e 42 f9` | ldr x8,[x19, #0x418] | `FALL_THROUGH`
<a id="insn-00bcc8d0"></a> `00bcc8d0` | `e8 00 00 b5` | cbnz x8,0x00bcc8ec | `CONDITIONAL_JUMP`
<a id="insn-00bcc8d4"></a> `00bcc8d4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00bcc8d8"></a> `00bcc8d8` | `e3 b6 ff d0` | adrp x3,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bcc8dc"></a> `00bcc8dc` | `63 f4 22 91` | add x3,x3,#0x8bd | `FALL_THROUGH`
<a id="insn-00bcc8e0"></a> `00bcc8e0` | `8c 38 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc8e4"></a> `00bcc8e4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcc8e8"></a> `00bcc8e8` | `60 0e 02 f9` | str x0,[x19, #0x418] | `FALL_THROUGH`
<a id="insn-00bcc8ec"></a> `00bcc8ec` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc8f0"></a> `00bcc8f0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcc8f4"></a> `00bcc8f4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcc8f8"></a> `00bcc8f8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcc8bc`](#insn-00bcc8bc) 範囲 `[['00bcc8bc', '00bcc8d3']]`
  - `CONDITIONAL_JUMP` [`00bcc8d0`](#insn-00bcc8d0) → [`00bcc8ec`](#insn-00bcc8ec)
  - `FALL_THROUGH` [`00bcc8d0`](#insn-00bcc8d0) → [`00bcc8d4`](#insn-00bcc8d4)
- ブロック [`00bcc8d4`](#insn-00bcc8d4) 範囲 `[['00bcc8d4', '00bcc8eb']]`
  - `FALL_THROUGH` [`00bcc8e8`](#insn-00bcc8e8) → [`00bcc8ec`](#insn-00bcc8ec)
- ブロック [`00bcc8ec`](#insn-00bcc8ec) 範囲 `[['00bcc8ec', '00bcc8f3']]`
  - `FALL_THROUGH` [`00bcc8f0`](#insn-00bcc8f0) → [`00bcc8f4`](#insn-00bcc8f4)
- ブロック [`00bcc8f4`](#insn-00bcc8f4) 範囲 `[['00bcc8f4', '00bcc8fb']]`

## 命令位置別の参照

- [`00bcc8bc`](#insn-00bcc8bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc8c0`](#insn-00bcc8c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc8cc`](#insn-00bcc8cc) → `01126418`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc8d0`](#insn-00bcc8d0) → [`00bcc8ec`](#insn-00bcc8ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc8dc`](#insn-00bcc8dc) → `002aa8bd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcc8e0`](#insn-00bcc8e0) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bcc8e8`](#insn-00bcc8e8) → `01126418`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc8ec`](#insn-00bcc8ec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcc8bc`](#insn-00bcc8bc)

~~~json
{
  "source": "00bcc8bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc8c0`](#insn-00bcc8c0)

~~~json
{
  "source": "00bcc8c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc8cc`](#insn-00bcc8cc)

~~~json
{
  "source": "00bcc8cc",
  "target": "01126418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc8d0`](#insn-00bcc8d0)

~~~json
{
  "source": "00bcc8d0",
  "target": "00bcc8ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc8dc`](#insn-00bcc8dc)

~~~json
{
  "source": "00bcc8dc",
  "target": "002aa8bd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa8bd",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002aa8bd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcc8e0`](#insn-00bcc8e0)

~~~json
{
  "source": "00bcc8e0",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc8e8`](#insn-00bcc8e8)

~~~json
{
  "source": "00bcc8e8",
  "target": "01126418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc8ec`](#insn-00bcc8ec)

~~~json
{
  "source": "00bcc8ec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
