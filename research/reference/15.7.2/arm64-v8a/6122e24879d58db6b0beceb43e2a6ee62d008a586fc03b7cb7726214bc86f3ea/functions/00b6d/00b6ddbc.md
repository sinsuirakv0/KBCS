# 00b6ddbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b6de84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6d/00b6de84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0073.md#compare-24caa9af633e0a254bee50e64a4a930d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6ddbc",
  "name": "_ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9cd9d9db9ce601c0a578f597f44728d8c6b6110440d508967f41acd222bdd740",
  "source_text_sha256": "9cd9d9db9ce601c0a578f597f44728d8c6b6110440d508967f41acd222bdd740",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6ddbc",
        "00b6ddfb"
      ]
    ],
    "bytes_sha256": "00cec10f33f675ca29a4e275e902d5d7df424f1b5a09a12a73b4c4d4454c6d01",
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

- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 551 bytes

~~~c

long _ZN8firebase4auth8metadata19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util16ClassRequirementE
               (void)

{
                    /* try { // try from 00b6ddc4 to 00c6de43 has its CatchHandler @ 00b6dd58 */
  if (DAT_010a19f8 == 0) {
    DAT_010a19f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             ();
  }
  return DAT_010a19f8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6ddbc"></a> `00b6ddbc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b6ddc0"></a> `00b6ddc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ddc4"></a> `00b6ddc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b6ddc8"></a> `00b6ddc8` | `b3 29 00 90` | adrp x19,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6ddcc"></a> `00b6ddcc` | `68 fe 44 f9` | ldr x8,[x19, #0x9f8] | `FALL_THROUGH`
<a id="insn-00b6ddd0"></a> `00b6ddd0` | `e8 00 00 b5` | cbnz x8,0x00b6ddec | `CONDITIONAL_JUMP`
<a id="insn-00b6ddd4"></a> `00b6ddd4` | `e4 03 03 2a` | mov w4,w3 | `FALL_THROUGH`
<a id="insn-00b6ddd8"></a> `00b6ddd8` | `03 ba ff 90` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00b6dddc"></a> `00b6dddc` | `63 40 19 91` | add x3,x3,#0x650 | `FALL_THROUGH`
<a id="insn-00b6dde0"></a> `00b6dde0` | `6c c0 01 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00b6dde4"></a> `00b6dde4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b6dde8"></a> `00b6dde8` | `60 fe 04 f9` | str x0,[x19, #0x9f8] | `FALL_THROUGH`
<a id="insn-00b6ddec"></a> `00b6ddec` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ddf0"></a> `00b6ddf0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b6ddf4"></a> `00b6ddf4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b6ddf8"></a> `00b6ddf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6ddbc`](#insn-00b6ddbc) 範囲 `[['00b6ddbc', '00b6ddc3']]`
  - `FALL_THROUGH` [`00b6ddc0`](#insn-00b6ddc0) → [`00b6ddc4`](#insn-00b6ddc4)
- ブロック [`00b6ddc4`](#insn-00b6ddc4) 範囲 `[['00b6ddc4', '00b6ddd3']]`
  - `CONDITIONAL_JUMP` [`00b6ddd0`](#insn-00b6ddd0) → [`00b6ddec`](#insn-00b6ddec)
  - `FALL_THROUGH` [`00b6ddd0`](#insn-00b6ddd0) → [`00b6ddd4`](#insn-00b6ddd4)
- ブロック [`00b6ddd4`](#insn-00b6ddd4) 範囲 `[['00b6ddd4', '00b6ddeb']]`
  - `FALL_THROUGH` [`00b6dde8`](#insn-00b6dde8) → [`00b6ddec`](#insn-00b6ddec)
- ブロック [`00b6ddec`](#insn-00b6ddec) 範囲 `[['00b6ddec', '00b6ddfb']]`

## 命令位置別の参照

- [`00b6ddbc`](#insn-00b6ddbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ddc0`](#insn-00b6ddc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ddcc`](#insn-00b6ddcc) → `010a19f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6ddd0`](#insn-00b6ddd0) → [`00b6ddec`](#insn-00b6ddec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dddc`](#insn-00b6dddc) → `002ad650`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b6dde0`](#insn-00b6dde0) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00b6dde8`](#insn-00b6dde8) → `010a19f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6ddec`](#insn-00b6ddec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6ddbc`](#insn-00b6ddbc)

~~~json
{
  "source": "00b6ddbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ddc0`](#insn-00b6ddc0)

~~~json
{
  "source": "00b6ddc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ddcc`](#insn-00b6ddcc)

~~~json
{
  "source": "00b6ddcc",
  "target": "010a19f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a19f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6ddd0`](#insn-00b6ddd0)

~~~json
{
  "source": "00b6ddd0",
  "target": "00b6ddec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dddc`](#insn-00b6dddc)

~~~json
{
  "source": "00b6dddc",
  "target": "002ad650",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad64c",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002ad64c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b6dde0`](#insn-00b6dde0)

~~~json
{
  "source": "00b6dde0",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6dde8`](#insn-00b6dde8)

~~~json
{
  "source": "00b6dde8",
  "target": "010a19f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a19f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6ddec`](#insn-00b6ddec)

~~~json
{
  "source": "00b6ddec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
