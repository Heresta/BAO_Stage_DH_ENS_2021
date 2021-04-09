<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:pr="http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15"
    xmlns="http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15"
    version="1.0">
    <xsl:output method="xml" indent="yes" encoding="UTF-8"/>
    
    <xsl:template match="pr:PcGts">
        <PcGts xmlns="http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15 http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15/pagecontent.xsd">
            <xsl:copy-of select="pr:Metadata"/>
            <xsl:apply-templates select="pr:Page"/>        
        </PcGts>
    </xsl:template>
    
    <xsl:template match="pr:Page">
        <xsl:copy>
            <xsl:copy-of select="pr:PrintSpace"/>
            <xsl:copy-of select="pr:ReadingOrder"/>
            <xsl:apply-templates select="pr:TextRegion"/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="pr:TextRegion">
        <xsl:element name="TextRegion">
            <xsl:if test="@type">
            <xsl:attribute name="type">
                <xsl:value-of select="@type"/>
            </xsl:attribute>
            </xsl:if>
            <xsl:attribute name="id">
                <xsl:value-of select="@id"/>
            </xsl:attribute>
            <xsl:attribute name="custom">
                <xsl:value-of select="@custom"/>
            </xsl:attribute>
            <xsl:copy-of select="pr:Coords"/>
            <xsl:element name="TextLine">
                <xsl:attribute name="id">
                    <xsl:value-of select="pr:TextLine/@id"/>
                </xsl:attribute>
                <xsl:if test="@primaryLanguage">
                <xsl:attribute name="primaryLanguage">
                    <xsl:value-of select="pr:TextLine/@primaryLanguage"/>
                </xsl:attribute>
                </xsl:if>
                <xsl:attribute name="custom">
                    <xsl:value-of select="pr:TextLine/@custom"/>
                </xsl:attribute>
                <xsl:copy-of select="pr:TextLine/pr:Coords"/>
                <xsl:copy-of select="pr:TextLine/pr:Baseline"/>
                <xsl:element name="Word">
                    <xsl:attribute name="custom">
                        <xsl:text>readingOrder {index:0;}</xsl:text>
                    </xsl:attribute>
                    <xsl:element name="Coords">
                        <xsl:attribute name="points">
                            <xsl:value-of select="pr:TextLine/pr:Coords/@points"/>
                        </xsl:attribute>
                        <xsl:element name="TextEquiv">
                            <xsl:element name="Unicode">
                                <xsl:value-of select="pr:TextEquiv/pr:Unicode"/>
                            </xsl:element>
                        </xsl:element>
                        <xsl:copy-of select="pr:TextLine/pr:TextStyle"/>
                    </xsl:element>
                </xsl:element>
            </xsl:element>
        </xsl:element>
    </xsl:template>

</xsl:stylesheet>
