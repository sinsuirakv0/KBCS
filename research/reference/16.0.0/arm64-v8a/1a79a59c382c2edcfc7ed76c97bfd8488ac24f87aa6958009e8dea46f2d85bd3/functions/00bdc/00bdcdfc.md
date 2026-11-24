# 00bdcdfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6d8fc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d8fc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-f11e22642efb663067e1a1c6ef042dc3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd224`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd224.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-6ee807ffe6e67536518e8cc13643a08b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdfc",
  "name": "_ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobject",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9b7d797b4b83d1c497249196c57c9b776db4b2be580cefa04d2286d15e653e8b",
  "source_text_sha256": "9b7d797b4b83d1c497249196c57c9b776db4b2be580cefa04d2286d15e653e8b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcdfc",
        "00bdce3f"
      ]
    ],
    "bytes_sha256": "9c421e4ae5df7d65d09f4e2c6597cb5d41648edcedc6c29994c777be159d2a04",
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
"%PG%com/google/firebase/auth/FirebaseUser"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 421 bytes

~~~c

long _ZN8firebase4auth4user10CacheClassEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126920 == 0) {
    DAT_01126920 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseUser",0);
  }
  return DAT_01126920;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcdfc"></a> `00bdcdfc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdce00"></a> `00bdce00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdce04"></a> `00bdce04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdce08"></a> `00bdce08` | `53 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdce0c"></a> `00bdce0c` | `68 92 44 f9` | ldr x8,[x19, #0x920] | `FALL_THROUGH`
<a id="insn-00bdce10"></a> `00bdce10` | `08 01 00 b5` | cbnz x8,0x00bdce30 | `CONDITIONAL_JUMP`
<a id="insn-00bdce14"></a> `00bdce14` | `63 b6 ff b0` | adrp x3,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdce18"></a> `00bdce18` | `63 e8 1e 91` | add x3,x3,#0x7ba | `FALL_THROUGH`
<a id="insn-00bdce1c"></a> `00bdce1c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdce20"></a> `00bdce20` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdce24"></a> `00bdce24` | `3b f7 01 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bdce28"></a> `00bdce28` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bdce2c"></a> `00bdce2c` | `60 92 04 f9` | str x0,[x19, #0x920] | `FALL_THROUGH`
<a id="insn-00bdce30"></a> `00bdce30` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdce34"></a> `00bdce34` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bdce38"></a> `00bdce38` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdce3c"></a> `00bdce3c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcdfc`](#insn-00bdcdfc) 範囲 `[['00bdcdfc', '00bdce13']]`
  - `CONDITIONAL_JUMP` [`00bdce10`](#insn-00bdce10) → [`00bdce30`](#insn-00bdce30)
  - `FALL_THROUGH` [`00bdce10`](#insn-00bdce10) → [`00bdce14`](#insn-00bdce14)
- ブロック [`00bdce14`](#insn-00bdce14) 範囲 `[['00bdce14', '00bdce2f']]`
  - `FALL_THROUGH` [`00bdce2c`](#insn-00bdce2c) → [`00bdce30`](#insn-00bdce30)
- ブロック [`00bdce30`](#insn-00bdce30) 範囲 `[['00bdce30', '00bdce3f']]`

## 命令位置別の参照

- [`00bdcdfc`](#insn-00bdcdfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce00`](#insn-00bdce00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce0c`](#insn-00bdce0c) → `01126920`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdce10`](#insn-00bdce10) → [`00bdce30`](#insn-00bdce30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce18`](#insn-00bdce18) → `002a97ba`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdce24`](#insn-00bdce24) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bdce2c`](#insn-00bdce2c) → `01126920`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdce30`](#insn-00bdce30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcdfc`](#insn-00bdcdfc)

~~~json
{
  "source": "00bdcdfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce00`](#insn-00bdce00)

~~~json
{
  "source": "00bdce00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce0c`](#insn-00bdce0c)

~~~json
{
  "source": "00bdce0c",
  "target": "01126920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126920",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdce10`](#insn-00bdce10)

~~~json
{
  "source": "00bdce10",
  "target": "00bdce30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce18`](#insn-00bdce18)

~~~json
{
  "source": "00bdce18",
  "target": "002a97ba",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a97b6",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a97b6",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdce24`](#insn-00bdce24)

~~~json
{
  "source": "00bdce24",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdce2c`](#insn-00bdce2c)

~~~json
{
  "source": "00bdce2c",
  "target": "01126920",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126920",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdce30`](#insn-00bdce30)

~~~json
{
  "source": "00bdce30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
