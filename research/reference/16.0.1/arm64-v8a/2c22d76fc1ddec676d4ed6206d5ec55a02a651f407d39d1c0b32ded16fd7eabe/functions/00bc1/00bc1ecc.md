# 00bc1ecc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bc1aa4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bc1/00bc1aa4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0080.md#compare-d3729b161c8bbad70fe4fc14cd7a3825)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc1f68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc1/00bc1f68.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0080.md#compare-e5298ca89f1ed2609c9531b80876c872)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc1ecc",
  "name": "_ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "11b7ddbcf2a2b335a21efe06f14caedb68f1a3a75a293ff35c429c1f51060555",
  "source_text_sha256": "11b7ddbcf2a2b335a21efe06f14caedb68f1a3a75a293ff35c429c1f51060555",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc1ecc",
        "00bc1f0b"
      ]
    ],
    "bytes_sha256": "21a06a0f1a5a4a183221d995e63ed601f0ac87eda1f29e4f26fb89a470cee543",
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

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/remoteconfig/FirebaseRemoteConfigValue"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 548 bytes

~~~c

long _ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allocatorISA_EEEE
               (void)

{
                    /* try { // try from 00bc1ed4 to 00cc1ed7 has its CatchHandler @ 00bc21dc */
  if (DAT_01126520 == 0) {
    DAT_01126520 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_01126520;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc1ecc"></a> `00bc1ecc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc1ed0"></a> `00bc1ed0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1ed4"></a> `00bc1ed4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc1ed8"></a> `00bc1ed8` | `33 2b 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc1edc"></a> `00bc1edc` | `68 92 42 f9` | ldr x8,[x19, #0x520] | `FALL_THROUGH`
<a id="insn-00bc1ee0"></a> `00bc1ee0` | `e8 00 00 b5` | cbnz x8,0x00bc1efc | `CONDITIONAL_JUMP`
<a id="insn-00bc1ee4"></a> `00bc1ee4` | `03 b8 ff 90` | adrp x3,0x2c1000 | `FALL_THROUGH`
<a id="insn-00bc1ee8"></a> `00bc1ee8` | `63 28 33 91` | add x3,x3,#0xcca | `FALL_THROUGH`
<a id="insn-00bc1eec"></a> `00bc1eec` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bc1ef0"></a> `00bc1ef0` | `08 64 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bc1ef4"></a> `00bc1ef4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bc1ef8"></a> `00bc1ef8` | `60 92 02 f9` | str x0,[x19, #0x520] | `FALL_THROUGH`
<a id="insn-00bc1efc"></a> `00bc1efc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1f00"></a> `00bc1f00` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bc1f04"></a> `00bc1f04` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc1f08"></a> `00bc1f08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc1ecc`](#insn-00bc1ecc) 範囲 `[['00bc1ecc', '00bc1ed3']]`
  - `FALL_THROUGH` [`00bc1ed0`](#insn-00bc1ed0) → [`00bc1ed4`](#insn-00bc1ed4)
- ブロック [`00bc1ed4`](#insn-00bc1ed4) 範囲 `[['00bc1ed4', '00bc1ee3']]`
  - `CONDITIONAL_JUMP` [`00bc1ee0`](#insn-00bc1ee0) → [`00bc1efc`](#insn-00bc1efc)
  - `FALL_THROUGH` [`00bc1ee0`](#insn-00bc1ee0) → [`00bc1ee4`](#insn-00bc1ee4)
- ブロック [`00bc1ee4`](#insn-00bc1ee4) 範囲 `[['00bc1ee4', '00bc1efb']]`
  - `FALL_THROUGH` [`00bc1ef8`](#insn-00bc1ef8) → [`00bc1efc`](#insn-00bc1efc)
- ブロック [`00bc1efc`](#insn-00bc1efc) 範囲 `[['00bc1efc', '00bc1f0b']]`

## 命令位置別の参照

- [`00bc1ecc`](#insn-00bc1ecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ed0`](#insn-00bc1ed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1edc`](#insn-00bc1edc) → `01126520`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc1ee0`](#insn-00bc1ee0) → [`00bc1efc`](#insn-00bc1efc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ee8`](#insn-00bc1ee8) → `002c1cca`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc1ef0`](#insn-00bc1ef0) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ef8`](#insn-00bc1ef8) → `01126520`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc1efc`](#insn-00bc1efc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc1ecc`](#insn-00bc1ecc)

~~~json
{
  "source": "00bc1ecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ed0`](#insn-00bc1ed0)

~~~json
{
  "source": "00bc1ed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1edc`](#insn-00bc1edc)

~~~json
{
  "source": "00bc1edc",
  "target": "01126520",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126520",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc1ee0`](#insn-00bc1ee0)

~~~json
{
  "source": "00bc1ee0",
  "target": "00bc1efc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ee8`](#insn-00bc1ee8)

~~~json
{
  "source": "00bc1ee8",
  "target": "002c1cca",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c1cc6",
  "offset": 4,
  "size": 63,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f72656d6f7465636f",
  "capture_start": "002c1cc6",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc1ef0`](#insn-00bc1ef0)

~~~json
{
  "source": "00bc1ef0",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc1ef8`](#insn-00bc1ef8)

~~~json
{
  "source": "00bc1ef8",
  "target": "01126520",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126520",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc1efc`](#insn-00bc1efc)

~~~json
{
  "source": "00bc1efc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
