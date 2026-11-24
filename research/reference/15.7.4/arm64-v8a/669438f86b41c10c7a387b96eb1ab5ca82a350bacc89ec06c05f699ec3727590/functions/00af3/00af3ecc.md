# 00af3ecc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00af3e88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af3/00af3e88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-f8b2fd7eca5291ba4fb7b45390a64bf3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b53c50`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b53/00b53c50.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0004.md#compare-792c55baf0017557d3a8379daf0451f1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af3ecc",
  "name": "_ZN8firebase4util11JCharToCharEP7_JNIEnvP8_jobject",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b215485ae769385424ccccbc15c4071daefc7e644b691d091b6852d239e6f92a",
  "source_text_sha256": "b215485ae769385424ccccbc15c4071daefc7e644b691d091b6852d239e6f92a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af3ecc",
        "00af3f33"
      ]
    ],
    "bytes_sha256": "bc73fcab8d25cd2017c0c6c8d859224c651a7fb50028146d6604ef2fdb3e8419",
    "instruction_count": 26,
    "instruction_bytes": 104,
    "body_bytes": 104,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde390](../00bde/00bde390.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 419 bytes

~~~c

undefined4 _ZN8firebase4util11JCharToCharEP7_JNIEnvP8_jobject(long *param_1,undefined8 param_2)

{
  char cVar1;
  undefined4 uVar2;
  
  uVar2 = _ZN7_JNIEnv14CallCharMethodEP8_jobjectP10_jmethodIDz(param_1,param_2,DAT_010a0688);
  cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
  if (cVar1 != '\0') {
    (**(code **)(*param_1 + 0x80))(param_1);
    (**(code **)(*param_1 + 0x88))(param_1);
  }
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af3ecc"></a> `00af3ecc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00af3ed0"></a> `00af3ed0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af3ed4"></a> `00af3ed4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00af3ed8"></a> `00af3ed8` | `68 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af3edc"></a> `00af3edc` | `02 45 43 f9` | ldr x2,[x8, #0x688] | `FALL_THROUGH`
<a id="insn-00af3ee0"></a> `00af3ee0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af3ee4"></a> `00af3ee4` | `2b a9 03 94` | bl 0x00bde390 | `UNCONDITIONAL_CALL`
<a id="insn-00af3ee8"></a> `00af3ee8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af3eec"></a> `00af3eec` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00af3ef0"></a> `00af3ef0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3ef4"></a> `00af3ef4` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00af3ef8"></a> `00af3ef8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3efc"></a> `00af3efc` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00af3f00"></a> `00af3f00` | `20 01 00 54` | b.eq 0x00af3f24 | `CONDITIONAL_JUMP`
<a id="insn-00af3f04"></a> `00af3f04` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af3f08"></a> `00af3f08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3f0c"></a> `00af3f0c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00af3f10"></a> `00af3f10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3f14"></a> `00af3f14` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af3f18"></a> `00af3f18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3f1c"></a> `00af3f1c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00af3f20"></a> `00af3f20` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3f24"></a> `00af3f24` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af3f28"></a> `00af3f28` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00af3f2c"></a> `00af3f2c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00af3f30"></a> `00af3f30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af3ecc`](#insn-00af3ecc) 範囲 `[['00af3ecc', '00af3f03']]`
  - `CONDITIONAL_JUMP` [`00af3f00`](#insn-00af3f00) → [`00af3f24`](#insn-00af3f24)
  - `FALL_THROUGH` [`00af3f00`](#insn-00af3f00) → [`00af3f04`](#insn-00af3f04)
- ブロック [`00af3f04`](#insn-00af3f04) 範囲 `[['00af3f04', '00af3f23']]`
  - `FALL_THROUGH` [`00af3f20`](#insn-00af3f20) → [`00af3f24`](#insn-00af3f24)
- ブロック [`00af3f24`](#insn-00af3f24) 範囲 `[['00af3f24', '00af3f33']]`

## 命令位置別の参照

- [`00af3ecc`](#insn-00af3ecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3ed0`](#insn-00af3ed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3edc`](#insn-00af3edc) → `010a0688`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af3ee4`](#insn-00af3ee4) → [`00bde390`](../00bde/00bde390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde390` · 推定シンボル `None` · 推定型 `None`
- [`00af3f00`](#insn-00af3f00) → [`00af3f24`](#insn-00af3f24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3f24`](#insn-00af3f24) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af3ecc`](#insn-00af3ecc)

~~~json
{
  "source": "00af3ecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3ed0`](#insn-00af3ed0)

~~~json
{
  "source": "00af3ed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3edc`](#insn-00af3edc)

~~~json
{
  "source": "00af3edc",
  "target": "010a0688",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0688",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af3ee4`](#insn-00af3ee4)

~~~json
{
  "source": "00af3ee4",
  "target": "00bde390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3f00`](#insn-00af3f00)

~~~json
{
  "source": "00af3f00",
  "target": "00af3f24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3f24`](#insn-00af3f24)

~~~json
{
  "source": "00af3f24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
