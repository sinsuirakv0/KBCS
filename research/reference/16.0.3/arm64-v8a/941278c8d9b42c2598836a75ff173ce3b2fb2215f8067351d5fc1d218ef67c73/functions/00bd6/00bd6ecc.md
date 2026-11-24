# 00bd6ecc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd5ed8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd5/00bd5ed8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0084.md#compare-39d971446842329a5e646897ab6e0db9)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd6ecc",
  "name": "_ZN8firebase4auth10googlecred13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d82ba483528237c5527fb4c255dcb1a28c5f1bdc36ff36a1aad2e57a7cacbb52",
  "source_text_sha256": "d82ba483528237c5527fb4c255dcb1a28c5f1bdc36ff36a1aad2e57a7cacbb52",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd6ecc",
        "00bd6f3b"
      ]
    ],
    "bytes_sha256": "8d1b32b9484647f3887949bc7c1d940541bb6e833b7dd8dd4e68e2ce27c3e4c6",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5bf90](../00c5b/00c5bf90.md)
- [00c5bfb0](../00c5b/00c5bfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/GoogleAuthProvider"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 661 bytes

~~~c

void _ZN8firebase4auth10googlecred13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01127b88 == 0) {
    DAT_01127b88 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/GoogleAuthProvider",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_01127b88,&DAT_00310050,1,&DAT_01127ba0,
             "com/google/firebase/auth/GoogleAuthProvider");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd6ecc"></a> `00bd6ecc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd6ed0"></a> `00bd6ed0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd6ed4"></a> `00bd6ed4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd6ed8"></a> `00bd6ed8` | `94 2a 00 b0` | adrp x20,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd6edc"></a> `00bd6edc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bd6ee0"></a> `00bd6ee0` | `81 c6 45 f9` | ldr x1,[x20, #0xb88] | `FALL_THROUGH`
<a id="insn-00bd6ee4"></a> `00bd6ee4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd6ee8"></a> `00bd6ee8` | `41 01 00 b5` | cbnz x1,0x00bd6f10 | `CONDITIONAL_JUMP`
<a id="insn-00bd6eec"></a> `00bd6eec` | `43 b7 ff f0` | adrp x3,0x2c1000 | `FALL_THROUGH`
<a id="insn-00bd6ef0"></a> `00bd6ef0` | `63 70 3a 91` | add x3,x3,#0xe9c | `FALL_THROUGH`
<a id="insn-00bd6ef4"></a> `00bd6ef4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd6ef8"></a> `00bd6ef8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bd6efc"></a> `00bd6efc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bd6f00"></a> `00bd6f00` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bd6f04"></a> `00bd6f04` | `2b 14 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd6f08"></a> `00bd6f08` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bd6f0c"></a> `00bd6f0c` | `80 c6 05 f9` | str x0,[x20, #0xb88] | `FALL_THROUGH`
<a id="insn-00bd6f10"></a> `00bd6f10` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd6f14"></a> `00bd6f14` | `c2 b9 ff d0` | adrp x2,0x310000 | `FALL_THROUGH`
<a id="insn-00bd6f18"></a> `00bd6f18` | `84 2a 00 b0` | adrp x4,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd6f1c"></a> `00bd6f1c` | `45 b7 ff f0` | adrp x5,0x2c1000 | `FALL_THROUGH`
<a id="insn-00bd6f20"></a> `00bd6f20` | `42 40 01 91` | add x2,x2,#0x50 | `FALL_THROUGH`
<a id="insn-00bd6f24"></a> `00bd6f24` | `84 80 2e 91` | add x4,x4,#0xba0 | `FALL_THROUGH`
<a id="insn-00bd6f28"></a> `00bd6f28` | `a5 70 3a 91` | add x5,x5,#0xe9c | `FALL_THROUGH`
<a id="insn-00bd6f2c"></a> `00bd6f2c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bd6f30"></a> `00bd6f30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd6f34"></a> `00bd6f34` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd6f38"></a> `00bd6f38` | `16 14 02 14` | b 0x00c5bf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd6ecc`](#insn-00bd6ecc) 範囲 `[['00bd6ecc', '00bd6eeb']]`
  - `CONDITIONAL_JUMP` [`00bd6ee8`](#insn-00bd6ee8) → [`00bd6f10`](#insn-00bd6f10)
  - `FALL_THROUGH` [`00bd6ee8`](#insn-00bd6ee8) → [`00bd6eec`](#insn-00bd6eec)
- ブロック [`00bd6eec`](#insn-00bd6eec) 範囲 `[['00bd6eec', '00bd6f0f']]`
  - `FALL_THROUGH` [`00bd6f0c`](#insn-00bd6f0c) → [`00bd6f10`](#insn-00bd6f10)
- ブロック [`00bd6f10`](#insn-00bd6f10) 範囲 `[['00bd6f10', '00bd6f3b']]`

## 命令位置別の参照

- [`00bd6ecc`](#insn-00bd6ecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6ed0`](#insn-00bd6ed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6ee0`](#insn-00bd6ee0) → `01127b88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd6ee8`](#insn-00bd6ee8) → [`00bd6f10`](#insn-00bd6f10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6ef0`](#insn-00bd6ef0) → `002c1e9c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd6f04`](#insn-00bd6f04) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bd6f0c`](#insn-00bd6f0c) → `01127b88`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd6f10`](#insn-00bd6f10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6f20`](#insn-00bd6f20) → `00310050`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6f24`](#insn-00bd6f24) → `01127ba0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd6f28`](#insn-00bd6f28) → `002c1e9c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd6f38`](#insn-00bd6f38) → [`00c5bf90`](../00c5b/00c5bf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd6ecc`](#insn-00bd6ecc)

~~~json
{
  "source": "00bd6ecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6ed0`](#insn-00bd6ed0)

~~~json
{
  "source": "00bd6ed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6ee0`](#insn-00bd6ee0)

~~~json
{
  "source": "00bd6ee0",
  "target": "01127b88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd6ee8`](#insn-00bd6ee8)

~~~json
{
  "source": "00bd6ee8",
  "target": "00bd6f10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6ef0`](#insn-00bd6ef0)

~~~json
{
  "source": "00bd6ef0",
  "target": "002c1e9c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c1e98",
  "offset": 4,
  "size": 48,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476f6f",
  "capture_start": "002c1e98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd6f04`](#insn-00bd6f04)

~~~json
{
  "source": "00bd6f04",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd6f0c`](#insn-00bd6f0c)

~~~json
{
  "source": "00bd6f0c",
  "target": "01127b88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd6f10`](#insn-00bd6f10)

~~~json
{
  "source": "00bd6f10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6f20`](#insn-00bd6f20)

~~~json
{
  "source": "00bd6f20",
  "target": "00310050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6f24`](#insn-00bd6f24)

~~~json
{
  "source": "00bd6f24",
  "target": "01127ba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd6f28`](#insn-00bd6f28)

~~~json
{
  "source": "00bd6f28",
  "target": "002c1e9c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c1e98",
  "offset": 4,
  "size": 48,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476f6f",
  "capture_start": "002c1e98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd6f38`](#insn-00bd6f38)

~~~json
{
  "source": "00bd6f38",
  "target": "00c5bf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
