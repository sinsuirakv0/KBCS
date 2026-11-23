# 00b7efbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7f084`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7f/00b7f084.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0004.md#compare-92f8558bc13c64cb8c217d46b8a310a1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7efbc",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEaSERKS3_",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "87721279f401cc3a527012c9eef0116bd99202df3f17decd80635b1e801ceeb9",
  "source_text_sha256": "87721279f401cc3a527012c9eef0116bd99202df3f17decd80635b1e801ceeb9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7efbc",
        "00b7f00b"
      ]
    ],
    "bytes_sha256": "8cca303165c75c6081ee2360e70cdaef31231dbfc2d93b671867d132e72433db",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be11e0](../00be1/00be11e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 662 bytes

~~~c

long _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEaSERKS3_(long param_1,long param_2)

{
  undefined8 uVar1;
  
  _ZNSt6__ndk16localeaSERKS0_(param_1 + 8,param_2 + 8);
  uVar1 = *(undefined8 *)(param_2 + 0x10);
  *(undefined8 *)(param_1 + 0x18) = *(undefined8 *)(param_2 + 0x18);
  *(undefined8 *)(param_1 + 0x10) = uVar1;
  uVar1 = *(undefined8 *)(param_2 + 0x20);
  *(undefined8 *)(param_1 + 0x28) = *(undefined8 *)(param_2 + 0x28);
  *(undefined8 *)(param_1 + 0x20) = uVar1;
  uVar1 = *(undefined8 *)(param_2 + 0x30);
  *(undefined8 *)(param_1 + 0x38) = *(undefined8 *)(param_2 + 0x38);
  *(undefined8 *)(param_1 + 0x30) = uVar1;
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7efbc"></a> `00b7efbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b7efc0"></a> `00b7efc0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b7efc4"></a> `00b7efc4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7efc8"></a> `00b7efc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b7efcc"></a> `00b7efcc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b7efd0"></a> `00b7efd0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b7efd4"></a> `00b7efd4` | `00 20 00 91` | add x0,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00b7efd8"></a> `00b7efd8` | `21 20 00 91` | add x1,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00b7efdc"></a> `00b7efdc` | `81 88 01 94` | bl 0x00be11e0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7efe0"></a> `00b7efe0` | `60 06 c0 3d` | ldr q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b7efe4"></a> `00b7efe4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b7efe8"></a> `00b7efe8` | `80 06 80 3d` | str q0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b7efec"></a> `00b7efec` | `60 0a c0 3d` | ldr q0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b7eff0"></a> `00b7eff0` | `80 0a 80 3d` | str q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00b7eff4"></a> `00b7eff4` | `60 0e c0 3d` | ldr q0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7eff8"></a> `00b7eff8` | `80 0e 80 3d` | str q0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00b7effc"></a> `00b7effc` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7f000"></a> `00b7f000` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b7f004"></a> `00b7f004` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b7f008"></a> `00b7f008` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7efbc`](#insn-00b7efbc) 範囲 `[['00b7efbc', '00b7f00b']]`

## 命令位置別の参照

- [`00b7efc0`](#insn-00b7efc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7efc4`](#insn-00b7efc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7efdc`](#insn-00b7efdc) → [`00be11e0`](../00be1/00be11e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be11e0` · 推定シンボル `None` · 推定型 `None`
- [`00b7effc`](#insn-00b7effc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7f000`](#insn-00b7f000) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7efc0`](#insn-00b7efc0)

~~~json
{
  "source": "00b7efc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7efc4`](#insn-00b7efc4)

~~~json
{
  "source": "00b7efc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7efdc`](#insn-00b7efdc)

~~~json
{
  "source": "00b7efdc",
  "target": "00be11e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7effc`](#insn-00b7effc)

~~~json
{
  "source": "00b7effc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7f000`](#insn-00b7f000)

~~~json
{
  "source": "00b7f000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
