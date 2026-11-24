# 00bd5ecc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b669cc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b66/00b669cc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0069.md#compare-aee0a4a420981b66d3479cbe009e1a7e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd62f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd6/00bd62f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0083.md#compare-0328ebdc72c8a5f2dcfcf20522502839)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd5ecc",
  "name": "_ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "40e5dd97aeebde6a2be40f13108dc214cc89d4335b14be71cd829d31155141ac",
  "source_text_sha256": "40e5dd97aeebde6a2be40f13108dc214cc89d4335b14be71cd829d31155141ac",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd5ecc",
        "00bd5f0f"
      ]
    ],
    "bytes_sha256": "43a0ed8a8f4349f43c08f266d7b58f62c5e32b54c944203207f65a02be7144a3",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
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
"%PG%com/google/firebase/auth/TwitterAuthProvider"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 452 bytes

~~~c

long _ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126708 == 0) {
    DAT_01126708 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/TwitterAuthProvider",0);
  }
  return DAT_01126708;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd5ecc"></a> `00bd5ecc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd5ed0"></a> `00bd5ed0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd5ed4"></a> `00bd5ed4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd5ed8"></a> `00bd5ed8` | `93 2a 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd5edc"></a> `00bd5edc` | `68 86 43 f9` | ldr x8,[x19, #0x708] | `FALL_THROUGH`
<a id="insn-00bd5ee0"></a> `00bd5ee0` | `08 01 00 b5` | cbnz x8,0x00bd5f00 | `CONDITIONAL_JUMP`
<a id="insn-00bd5ee4"></a> `00bd5ee4` | `63 b6 ff 90` | adrp x3,0x2a1000 | `FALL_THROUGH`
<a id="insn-00bd5ee8"></a> `00bd5ee8` | `63 2c 31 91` | add x3,x3,#0xc4b | `FALL_THROUGH`
<a id="insn-00bd5eec"></a> `00bd5eec` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bd5ef0"></a> `00bd5ef0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bd5ef4"></a> `00bd5ef4` | `07 13 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bd5ef8"></a> `00bd5ef8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd5efc"></a> `00bd5efc` | `60 86 03 f9` | str x0,[x19, #0x708] | `FALL_THROUGH`
<a id="insn-00bd5f00"></a> `00bd5f00` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd5f04"></a> `00bd5f04` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd5f08"></a> `00bd5f08` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd5f0c"></a> `00bd5f0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd5ecc`](#insn-00bd5ecc) 範囲 `[['00bd5ecc', '00bd5ee3']]`
  - `CONDITIONAL_JUMP` [`00bd5ee0`](#insn-00bd5ee0) → [`00bd5f00`](#insn-00bd5f00)
  - `FALL_THROUGH` [`00bd5ee0`](#insn-00bd5ee0) → [`00bd5ee4`](#insn-00bd5ee4)
- ブロック [`00bd5ee4`](#insn-00bd5ee4) 範囲 `[['00bd5ee4', '00bd5eff']]`
  - `FALL_THROUGH` [`00bd5efc`](#insn-00bd5efc) → [`00bd5f00`](#insn-00bd5f00)
- ブロック [`00bd5f00`](#insn-00bd5f00) 範囲 `[['00bd5f00', '00bd5f0f']]`

## 命令位置別の参照

- [`00bd5ecc`](#insn-00bd5ecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5ed0`](#insn-00bd5ed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5edc`](#insn-00bd5edc) → `01126708`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd5ee0`](#insn-00bd5ee0) → [`00bd5f00`](#insn-00bd5f00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5ee8`](#insn-00bd5ee8) → `002a1c4b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd5ef4`](#insn-00bd5ef4) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bd5efc`](#insn-00bd5efc) → `01126708`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd5f00`](#insn-00bd5f00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd5ecc`](#insn-00bd5ecc)

~~~json
{
  "source": "00bd5ecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5ed0`](#insn-00bd5ed0)

~~~json
{
  "source": "00bd5ed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5edc`](#insn-00bd5edc)

~~~json
{
  "source": "00bd5edc",
  "target": "01126708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126708",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd5ee0`](#insn-00bd5ee0)

~~~json
{
  "source": "00bd5ee0",
  "target": "00bd5f00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5ee8`](#insn-00bd5ee8)

~~~json
{
  "source": "00bd5ee8",
  "target": "002a1c4b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1c47",
  "offset": 4,
  "size": 49,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f547769",
  "capture_start": "002a1c47",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd5ef4`](#insn-00bd5ef4)

~~~json
{
  "source": "00bd5ef4",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd5efc`](#insn-00bd5efc)

~~~json
{
  "source": "00bd5efc",
  "target": "01126708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126708",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd5f00`](#insn-00bd5f00)

~~~json
{
  "source": "00bd5f00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
